def closest_pair(points):
    
    points_sorted_by_x = sorted(points, key=lambda point: point[0])
    
    return closest_pair_recursive(points_sorted_by_x)

def closest_pair_recursive(points_sorted_by_x):
    
    if len(points_sorted_by_x) <= 3:
        return brute_force_closest_pair(points_sorted_by_x)
    
    
    mid = len(points_sorted_by_x) // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]
    
   
    left_closest = closest_pair_recursive(left_half)
    right_closest = closest_pair_recursive(right_half)
    
   
    min_distance = min(distance(left_closest), distance(right_closest))
    
   
    split_closest = closest_split_pair(points_sorted_by_x, mid, min_distance)
    
    
    return min(left_closest, right_closest, split_closest, key=lambda pair: distance(pair))

def brute_force_closest_pair(points):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance((points[i], points[j])) < min_distance:
                min_distance = distance((points[i], points[j]))
                closest_pair = (points[i], points[j])
    return closest_pair

def distance(pair):
    p1, p2 = pair
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def closest_split_pair(points_sorted_by_x, mid, delta):
    mid_x = points_sorted_by_x[mid][0]
    in_strip = [point for point in points_sorted_by_x if abs(point[0] - mid_x) < delta]
    in_strip.sort(key=lambda point: point[1])  # Sort by y-coordinate
    
    min_distance = delta
    closest_pair = None
    
    for i in range(len(in_strip)):
        for j in range(i + 1, len(in_strip)):
            if (in_strip[j][1] - in_strip[i][1]) >= min_distance:
                break
            d = distance((in_strip[i], in_strip[j]))
            if d < min_distance:
                min_distance = d
                closest_pair = (in_strip[i], in_strip[j])
                
    return closest_pair if closest_pair else (points_sorted_by_x[mid - 1], points_sorted_by_x[mid])

points = [
    (2, 2),  
    (2, 8),  
    (5, 5),  
    (6, 3),  
    (6, 7),  
    (7, 4),  
    (7, 9)   
]

result = closest_pair(points)
print(result)

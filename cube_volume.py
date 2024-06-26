import math
def cube_volume(r, h):
    import math
    max_side_by_height = h
    max_side_by_diameter = r*math.sqrt(2)
    
    side_length = min(max_side_by_height, max_side_by_diameter)
    
    volume = side_length**3
    
    return volume
    
  
    
radius = int(input())
height = int(input())
print(cube_volume(radius, height))
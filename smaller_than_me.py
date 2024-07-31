def smaller(arr):
    
    sorted_unique_arr = sorted(set(arr))
    rank_map = {num: rank for rank, num in enumerate(sorted_unique_arr)}
    
    # Create a list to store the counts of numbers
    counts = [0] * len(arr)
    
    # Iterate from right to left in the array
    result = []
    for num in reversed(arr):
        rank = rank_map[num]
        result.append(sum(counts[:rank]))
        counts[rank] += 1
    
    return result[::-1]

print(smaller([5, 4, 3, 2, 1]))  
print(smaller([1, 2, 0]))        

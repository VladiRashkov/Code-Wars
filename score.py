def score(dice):
    sorted_nums = sorted(dice)
    points = 0
    
    
    for i in range(1, 7):
        if sorted_nums.count(i) >= 3:
            if i == 1:
                points += 1000
            else:
                points += i * 100
            
            for _ in range(3):
                sorted_nums.remove(i)
    
    
    points += sorted_nums.count(1) * 100
    points += sorted_nums.count(5) * 50
    
    return points

# numbers = list(map(int, input().split(",")))
print(score([2, 4, 4, 5, 4]))

def move_zeros(lst):
    numbers = []
    moved_zeros = []
    for i in lst:
        
        if i==0:
            moved_zeros.append(i)
        else:
            numbers.append(i)
            
    final_list = numbers + moved_zeros
    return final_list


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
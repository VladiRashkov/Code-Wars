def max_num(l):
    max_num = 0
    for i in l:
        if i>max_num:
            max_num=i
    return max_num

print(max_num(list(map(int, input().split(',')))))
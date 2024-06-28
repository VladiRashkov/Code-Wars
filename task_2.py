def sentnce(s):
    sum=0
    for i in s:
        try:
            sum+=float(i)
        except:
            continue
    return sum

print(sentnce(input().split(' ')))
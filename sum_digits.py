def sum_digits(n):
    
    abs_n = abs(n)
    sum = 0
    while abs_n!=0:
        digit = abs_n%10
        sum+=digit
        abs_n = abs_n//10
    return sum

print(sum_digits(int(input())))
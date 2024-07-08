def narcissistic(n):
    sum = 0
    original_num = n
    lenght = len(str(n))
    while n!=0:
        digit = n%10
        n=n//10
        sum+=digit**lenght
    return True if original_num==sum else False

print(narcissistic(int(input())))
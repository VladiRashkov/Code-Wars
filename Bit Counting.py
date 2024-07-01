# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    binary_num = ''
    sum=0
    while n!= 0:
        number = n%10
        n=n//10
        while True:
            if number%2==1:
                binary_num+='1'
                number = number//2
            else:
                binary_num+='0'
                number = number//2
            
            if number == 0:
                break
                
    for i in range(len(binary_num)):
        if binary_num[i]=='1':
            sum+=1
    return sum
    

print(count_bits(int(input())))
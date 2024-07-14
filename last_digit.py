#first solution
def last_digit(n1, n2):
    return pow( n1, n2, 10 )
print(last_digit(4,2))


#second solution


def last_digit(n1, n2):
    if n2 == 0:
        return 1
    
    last_digit_n1 = n1 % 10
    
    if n2 % 4 == 0:
        effective_power = 4
    else:
        effective_power = n2 % 4
    
    result = (last_digit_n1 ** effective_power) % 10
    
    return result
    

print(last_digit(4, 2)) 

# Define a function that takes in two non-negative integers 
# 𝑎
# a and 
# 𝑏
# b and returns the last decimal digit of 
# 𝑎
# 𝑏
# a 
# b
#  . Note that 
# 𝑎
# a and 
# 𝑏
# b may be very large!

# For example, the last decimal digit of 
# 9
# 7
# 9 
# 7
#   is 
# 9
# 9, since 
# 9
# 7
# =
# 4782969
# 9 
# 7
#  =4782969. The last decimal digit of 
# (
# 2
# 200
# )
# 2
# 300
# (2 
# 200
#  ) 
# 2 
# 300
 
#  , which has over 
# 1
# 0
# 92
# 10 
# 92
#   decimal digits, is 
# 6
# 6. Also, please take 
# 0
# 0
# 0 
# 0
#   to be 
# 1
# 1.

# You may assume that the input will always be valid.

# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6
import itertools

def next_bigger(number):
    
    if number<=9:
        return -1   
    
    num_str = str(number)
    digits = list(num_str)
    
    
    permutations = itertools.permutations(digits)
    
    
    variations = [int(''.join(p)) for p in permutations]
    

    unique_variations = list(set(variations))
    sorted_list = sorted(unique_variations)
    
    for i in sorted_list:
        if i > number:
            return i
    
    return -1        
    

print(next_bigger(int(input())))


# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

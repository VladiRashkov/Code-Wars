import itertools
import sys

def next_number(number):
    str_number = str(number)
    digits = list(str_number)
    permutations = itertools.permutations(digits)
    all_nums = ["".join(p) for p in permutations]
    unique_nums = list(set(all_nums))
    
   
    unique_nums = list(map(int, unique_nums)) 
    sorted_unique =sorted(unique_nums, reverse=True)
    found_num = False
    
    for i in sorted_unique:
        if i==number:
            found_num=True
            continue
        if found_num:
            return i
            
    
    return -1

number = int(input("Enter a number: "))
print(next_number(number))


# Description:
# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# For example:

# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
import itertools
def middle_permutation(word):
    
    list_var = list(word)
    permutations = itertools.permutations(list_var)
    unique_words = sorted(list(set(permutations)))
    str_unique = [''.join (x) for x in unique_words]
    
    middle_index = (len(str_unique)-1)//2
    middle_element = str_unique[middle_index]
    return middle_element

print(middle_permutation('abc'))

Task
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation.
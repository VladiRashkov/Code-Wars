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


import itertools

def permutations(s):
    symbols = list(s)
    variants = itertools.permutations(symbols)
    
    unique_var = set()
    
    for p in variants:
        unique_var.add("".join(p))
    
    
    return sorted(unique_var)
word = 'aabb'
print(permutations(word))
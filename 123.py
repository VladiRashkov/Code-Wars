import math
def nb_year(p0, percent, aug, p):
    years = 0
    while p0<p:
        p0+=math.floor(p0*(percent/100)+aug)
        
        years+=1

    return years

p0 = int(input())
percent = int(input())
aug = int(input())
p = int(input())

    
    
print(nb_year(p0, percent, aug, p))
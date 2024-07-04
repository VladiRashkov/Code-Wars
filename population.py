def nb_year(p0, percent, aug, p):
    years = 0
    while p0<p:
        p0+=p0*percent+aug
        years+=1

    return years

p0 = int(input())
percent = float(input())/100
aug = int(input())
p = int(input())

    
    
print(nb_year(p0, percent, aug, p))
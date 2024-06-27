import math

def equable_triangle(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    perimeter = a+b+c
    
    return perimeter == area

print(equable_triangle(2,2,3))
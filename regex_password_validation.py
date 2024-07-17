import re

def expression(s):
    regex = r'^(?=.*[A-Z, a-z,0-9])[A-Z, a-z,0-9]{6,}$'
    
    if re.search(regex, s):
        return True
    else:
        return False
        

print(expression(input()))
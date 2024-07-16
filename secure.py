
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore
def alphanumeric(password):
    if len(password)==0:
        return False
    
    pattern = r'[`!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>\/?~\n]'
    alpha=False
    numeric=False
    for i in password:
        if i == " ":
            return False
        if i.isalpha():
            alpha=True
        elif i.isnumeric():
            numeric=True
        elif i in pattern:
            return False
        if i =="\n":
            return False
    
    if alpha or numeric:
        return True
    else:
        return False

print(alphanumeric(input()))
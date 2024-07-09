def replace(s):
    numbers = []
    for char in s:
        if not char.isalpha():
            continue
        else:
            if char.isupper():
                number = ord(char)-64
                numbers.append(number)
            else:
                number = ord(char)-96
                numbers.append(number)
    return " ".join(map(str,numbers))
print(replace(input()))
def my_parse_int(strn):
    stripped = strn.strip()
    for i in stripped:
        try:
            number = int(i)
        except:
            return 'NaN'
            
    return number


print(my_parse_int(input()))
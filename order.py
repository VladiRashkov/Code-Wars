def order(s):
    if not s:
        return ""
    string_list = s.split(" ")
    
    sorted_list = [None] * len(string_list)

    for word in string_list:
        for char in word:
            if char.isdigit():
                sorted_list[int(char)-1]=word
              
    return " ".join(sorted_list)

print(order("is2 Thi1s T4est 3a"))
def order(s):
    string_list = s.split(" ")
    sorted_list = [None] * len(string_list)

    for word in string_list:
        for char in word:
            if char.isdigit():
                sorted_list[int(char)-1]=word
    return " ".join(sorted_list)

print(order(input()))
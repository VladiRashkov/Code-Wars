def duplicate_count(text):
    clean_text = text.lower()
    char_count = {}
    for char in clean_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    duplicate_count = sum(1 for count in char_count.values() if count > 1)
    
    return duplicate_count
 
print(duplicate_count('Indivisibilities'))
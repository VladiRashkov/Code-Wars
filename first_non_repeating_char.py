def first_non_repeating_letter(s):
    lowered = s.lower()
    i = 0
    while i < len(s):
        count = 0
        for j in range(len(s)):
            if lowered[i] == lowered[j] and i != j:
                count += 1
                i += 1  
                break
        if count == 0:
            return s[i]
        
        if count == 0:
            i += 1
    return ''


print(first_non_repeating_letter(input()))

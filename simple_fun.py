def happy_or_not(w):
    for i in range(len(w)):
        if w[i] == 'g':
            if (i > 0 and w[i-1] == 'g') or (i < len(w)-1 and w[i+1] == 'g'):
                continue
            else:
                return False
    return True

word = input()
print(happy_or_not(word))

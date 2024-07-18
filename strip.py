def strip_comments(strng, markers):
    lines = strng.split('\n')
    result = []

    for line in lines:
        
        min_pos = len(line)
        for marker in markers:
            pos = line.find(marker)
            if pos != -1 and pos < min_pos:
                min_pos = pos
        
        result.append(line[:min_pos].rstrip())
    
    return '\n'.join(result)


output = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(output)

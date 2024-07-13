def solution(numbers):
    if not numbers:
        return ""

    result = []
    start = numbers[0]
    prev = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] != prev + 1:
            if prev == start:
                result.append(str(start))
            elif prev == start + 1:
                result.append(str(start))
                result.append(str(prev))
            else:
                result.append(f"{start}-{prev}")
            start = numbers[i]
        prev = numbers[i]

    
    if prev == start:
        result.append(str(start))
    elif prev == start + 1:
        result.append(str(start))
        result.append(str(prev))
    else:
        result.append(f"{start}-{prev}")

    return ",".join(result)


numbers = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
print(solution(numbers))


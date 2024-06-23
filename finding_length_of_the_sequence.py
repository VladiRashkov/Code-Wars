def length_of_sequence(arr, n):
    first_occurrence_index = -1
    second_occurrence_index = -1
    count = 0

    for i in range(len(arr)):
        if arr[i] == n:
            first_occurrence_index = i
            break
    if first_occurrence_index == -1:
        return 0

    for j in range(first_occurrence_index+1, len(arr)):
        if arr[j] == n:
            second_occurrence_index = j
            count += 1
            if count >= 2:
                return 0

    if second_occurrence_index == -1:
        return 0

    count = second_occurrence_index - first_occurrence_index + 1

    return count


numbers = list(map(int, input().split(',')))
n = int(input())

print(length_of_sequence(numbers, n))

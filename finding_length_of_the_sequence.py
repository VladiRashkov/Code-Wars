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


# As part of this kata, you need to find the length of the sub-array that begins and ends with the specified number.

# For example, if the array arr is [0, -3, 7, 4, 0, 3, 7, 9], finding the length of the sub-array that begins and ends with 7s would return 5.

# For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

# If there are less or more than two occurrences of the number to search for, return 0.
#123141541
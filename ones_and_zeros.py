def binary_array_to_number(nums):
    sum=0
    for i in range(len(nums)):
        sum+=nums[len(nums)-1-i]*(2**i)
    return sum

print(binary_array_to_number(list(map(int, input().split(',')))))
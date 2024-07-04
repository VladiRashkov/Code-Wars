def smaller(arr):
    new_arr = []
    
    for i in range(len(arr)):
        count=0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                count+=1
           
        new_arr.append(count)
              
    
    return new_arr
        


print(smaller(list(map(int, input().split(',')))))
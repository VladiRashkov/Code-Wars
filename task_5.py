def print_pyramid(N):
    current_number = 1
    level = 1

    while current_number <= N:
        
        spaces = ' ' * (N - (level * (level - 1)) // 2)
        
        
        for i in range(level):
            if current_number > N:
                break
            print(spaces, end='')
            print(current_number, end=' ')
            current_number += 1
            spaces = ''  
        print()  
        level += 1  


print_pyramid(10)
print_pyramid(18)

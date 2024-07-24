def find_word(board, word):
    rows = len(board)
    cols = len(board[0])
    word_len = len(word)
    
    def dfs(row, col, index, visited):
        if index == word_len:
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] != word[index]:
            return False
        
        visited.add((row, col))
        # Explore all 8 possible directions
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # vertical and horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1) # diagonal
        ]
        
        for dr, dc in directions:
            if dfs(row + dr, col + dc, index + 1, visited):
                return True
        
        visited.remove((row, col))
        return False
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:  # Start DFS if the first letter matches
                if dfs(row, col, 0, set()):
                    return True
    return False

# Test cases
board = [
    ["I", "L", "A", "W"],
    ["B", "N", "G", "E"],
    ["I", "U", "A", "O"],
    ["A", "S", "R", "L"]
]

print(find_word(board, "BINGO"))  # Output should be True
print(find_word(board, "LINGO"))  # Output should be True
print(find_word(board, "ILNBIA"))  # Output should be True
print(find_word(board, "BUNGIE"))  # Output should be False
print(find_word(board, "BINS"))  # Output should be False
print(find_word(board, "SINUS"))  # Output should be False

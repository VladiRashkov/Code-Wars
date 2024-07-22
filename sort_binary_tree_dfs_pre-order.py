from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

root1 = Node(Node(None, None, 1), Node(None, None, 3), 8)
root1 = Node(root1, Node(Node(None, None, 4), Node(None, None, 5), 9), 2)
print(level_order_traversal(root1))  

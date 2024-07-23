from collections import deque


class Node():
    def __init__(self, L, R, V):
        self.left = L
        self.right = R
        self.value = V
        
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


root1 = Node(Node(None,None,1),Node(None,None,3),8)
root2 = Node(Node(None,None,9),Node(None, None,4),5)
root3 = Node(root1,root2,2)
print(level_order_traversal(root3))
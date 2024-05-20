from binarytree import Node

a = Node('a')

b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b

a.right = c

b.left = d
b.right = e
c.right = f

def bfs(root):
    if root is None:
        return []
    
    
    # create a queue
    queue = [root]
    
    tree = []
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        tree.append(current_node.value)
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
            
    return tree
            


answer = bfs(a)
print(answer)

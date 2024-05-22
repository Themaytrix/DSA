from binarytree import Node


a = Node(3)
# print(a.value)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b

a.right = c

b.left = d
b.right = e
c.right = f


def dfs_treesum(root):
    
    if root is None:
        return 0
    
    return root.value + dfs_treesum(root.left) + dfs_treesum(root.right)
    
# print(dfs_treesum(a))

def bfs_treesum(root):
    if root is None:
        return 0
    queue = [root]
    current_sum = 0
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        current_sum += current_node.value
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return current_sum
            
bfs_treesum(a)
    
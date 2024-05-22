from binarytree import Node

a = Node(5)
# print(a.value)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(15)
f = Node(12)

a.left = b

a.right = c

b.left = d
b.right = e
c.right = f

infinity = float('infinity')
def treemin_val(root):
    
    if root is None:
        return infinity
    
    return min(root.value, treemin_val(root.left),treemin_val(root.right))
    
    
    

print(treemin_val(a))
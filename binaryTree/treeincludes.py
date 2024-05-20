# using depth first search approach

from binarytree import Node

a = Node('a')
# print(a.value)
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')


"""
        a
       /  \
      b     c
     / \      \
    d   e       f
      
"""

a.left = b

a.right = c

b.left = d
b.right = e
c.right = f


def recursive_includes(root, target):
    if root is None:
        return False
    # print(root.value)
    if root.value == target:
        return True
    
    if recursive_includes(root.left,target) or recursive_includes(root.right,target):
        return True
    else:
        return False
    
    # return False

print(recursive_includes(a,'x'))

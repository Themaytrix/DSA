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
"""
        5
      /   \
     11    3
    /  \    \
   4    15   12
"""


def max_path(root):
    # check if leaf is null return a negative infinity
    if root is None:
        return float("-inf")
    # if end of node has no children, return the node itself
    if (root.left is None and root.right is None):
        return root.value
    maxleaf = max(max_path(root.left), max_path(root.right))
    return root.value + maxleaf

print(max_path(a))
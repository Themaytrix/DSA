
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.value
        

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

print(a)
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

# iterative approach
def depthfirstvalue(root):
    # implementing a depthfirstvalue using a stack. 
    stack = [root]
    
    # iterate over the stack while it's not empty
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.right:
            stack.append(current_node.right)
        elif current_node.left:
            stack.append(current_node.left)

        print(current_node)
        

depthfirstvalue(a)
        
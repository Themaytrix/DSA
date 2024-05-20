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

# iterative approach
def depthfirstvalue(root):
    # implementing a depthfirstvalue using a stack. 
    if root == None:
        return []
    stack = [root]
   
    tree = []
    
    # iterate over the stack while it's not empty
    while len(stack) > 0:
        current_node = stack.pop()
        tree.append(current_node.value)
        # print(tree)
        
        
        if current_node.right:
            
            stack.append(current_node.right)
            
        if current_node.left:
            
            stack.append(current_node.left)
            # print(current_node)
            
    return tree

# recursive approach
tree = []
def recursive_dfs(root):
    # tree.append(root.value)
    # print(tree)
    if root is None:
        return 
    tree.append(root.value)
    recursive_dfs(root.left)
    recursive_dfs(root.right)
    return tree
    
answer = recursive_dfs(a)
print(answer)
            
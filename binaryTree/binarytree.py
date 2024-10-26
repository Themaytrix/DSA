
from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    # def __str__(self) -> str:
    #     return self.value
        

    def insert(self,value):
        # insert if the root is empty
        if self.value is None:
            self.value = value
        else:
            # check if the left and right nodes are filled
            
            if value < self.value:
                # check if node is filled or not
                if self.left is None:
                    # if not filled. construct new node at left and insert value to left
                    self.left = Node(value)
                else:
                    # recursively call left insert till you find an empty node
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
                    
                    
def in_order_traversal(r):
    #base case for recursion
    if r is None:
        return 
    # lnr traversal.
    in_order_traversal(r.left)
    print(r.value)
    in_order_traversal(r.right)
    
def pre_order_traversal(r):
    if r is None:
        return
    else:
        print(r.value)
        pre_order_traversal(r.left)
        pre_order_traversal(r.right)
        
# In making adjacency list -- Inorder Traversal??
def makelist(r):
    if r is None:
        return
    else:
        # istantiaite a key and empty list on every visited node
        d[r.value] = []
        makelist(r.left)
        # check if there is a left or right child to the node
        if r.left:
            # set the current key with its values
            d[r.value].append(r.left.value)
        if r.right:
            d[r.value].append(r.right.value)
            
        makelist(r.right)
    
    return d

d = {}

# breathfirst search. Use queues

def bsf(root, alist):
    
    # instantiate queue
    queue = deque()
    visited = []
    queue.append(root.value)
    
    while len(queue) > 0:
        node = queue.popleft()
        print(node)
        visited.append(node)
        for i in alist[node]:
            queue.append(i)
    
    return visited


def dfs(root,visit):
    
    
    if root is None:
        return
    
    # target first root and execute command on first node
    visit.append(root.value)
    # continue down the path with recursion
    dfs(root.left,visit)
    dfs(root.right,visit)
    
    return visit

def stack_bfs_maxdpth(root):
    
    stack = [root]
    
    if root is None:
        return 0
    
    level = 0
    
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        level += 1
            
    return level

def inversebt(root):
    if root is None:
        return
    
    else:
        temp = root.left.value
        root.left.value = root.right.value
        root.right.value = temp
        
        inversebt(root.left)
        inversebt(root.right)
        
def buildTree(preorder,inorder,ans):
    if not preorder or not inorder:
        return None
    
    
    # set root to be intial node of preorder
    root = Node(preorder[0])
    # find the mid element in the inorder tree i.e point that splits tree to left and right we want the index
    ans.append(root.value)
    
    print(ans)
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid],ans)
    
    # print(root.value)
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:],ans)
        
    
    # print(root.value)
    return root
    



if __name__ == "__main__":
    
    # root = Node('g')
    # root.insert('c')
    # root.insert('b')
    # root.insert('e')
    # root.insert('i')
    # root.insert('h')
    # root.insert('j')
    # root.insert('a')
    # root.insert('d')
    # root.insert('f')
    # root.insert('k')
    
    
    
    # # make adjacency list
    # alist = makelist(root)
    # # for i in alist:
    # #     print(f"{i}:{d[i]}")
    
    # # print(bsf(root,alist))
    # visit =[]
    # print(stack_bfs_maxdpth(root))
    ans = []
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    buildTree(preorder,inorder,ans)

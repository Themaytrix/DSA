"""
Input:
                  		1(0)
              	2(-1)     		3(1)
            (-2)4       5(0)    6(0)    7(2) 
                        
      Output:
      4
      2 8 
      1 5 6 
      3 
      7 


"""

from collections import defaultdict
from collections import deque
class Node():
      def __init__(self,root,left=None,right=None):
            self.val = root
            self.left = left
            self.right = right
 
node4 = Node(4)
node5 = Node(5)
node2 = Node(2,node4,node5)
node6 = Node(6)
node7 = Node(7)
node3 = Node(3,node6,node7)            
node1 = Node(1,node2,node3)

adj = defaultdict(list)




def printsth(node,index):
      
      if node == None:
            return 
      adj[index].append(node.val)
      printsth(node.left,index-1)
      printsth(node.right,index+1)      
index = 0
            
# printsth(node1,index)

# for index in sorted(adj):
#       for a in adj[index]:
#             print(a)
      


def bfsprint(node,index):
      
      if not node:
            return
      
      queue = deque()
      queue.append((node,index))
      
      while queue:
            current_node,index = queue.popleft()
            
            adj[index].append(current_node.val)
            
            if current_node.left:
                  queue.append((current_node.left,index-1))
            if current_node.right:
                  queue.append((current_node.right,index+1))
                  
      
      # while queue:
      #       c_n,index = queue.popleft()
            
      #       if c_n.left:
                  
      
# bfsprint(node1,index)

# print(adj)

def getheight(root):
      stack = [[root,1]]
      res = 0
      
      while stack:
            node,depth = stack.pop()
            
            if node:
                  res = max(res,depth)
                  stack.append([node.left,depth+1])
                  stack.append([node.right, depth+1])
                  
      return res

print(getheight(node1))
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrtoBST(arr):
    # approach using binary search
    bt = []
    
    
    def helper(l,h):
        if l>h:
            return None
        m = (l+h) // 2
        
        root = TreeNode(arr[m])
        
        bt.append(root.val)
        
        
        
        root.left = helper(l, m-1)
        
        root.right = helper(m+1,h)
        
        
            
            
    helper(0,len(arr)-1)
    return bt
        
        
    


   
arr = [-10,-3,0,5,9]
# arr2 = [-10,-3]   
sortedArrtoBST(arr)

# print(arr2[:len(arr)//2-1])
    
    
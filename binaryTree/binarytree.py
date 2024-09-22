
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



if __name__ == "__main__":
    
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('e')
    root.insert('h')
    root.insert('j')
    root.insert('a')
    root.insert('d')
    root.insert('f')
    root.insert('k')
    
    # in_order_traversal(root)
    pre_order_traversal(root)


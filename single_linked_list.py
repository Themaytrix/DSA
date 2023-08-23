class Node:
    """
    An object for storing a single node of a linked list.
    Models two attribures - data and the link to the next node in the list
    """
    data = None
    next_node = None
    
    def __init__(self,data) -> None:
        self.data = data
    
    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        
        """
        current = self.head
        count = 0
    
        while current:
            count += 1
            current= current.next_node
            
        return count
    
    def add(self,data):
        """
        Adds a new_node to the list as the head and assigns already existing node as the next node
        takes 0(1) - constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
from nodes import Node

a = Node('a')
# print(a.value)
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d


# iterative traversal

def travlinkelist(head):
    currentnode = head
    
    while currentnode !=  None:
        print(currentnode.val)
        currentnode = currentnode.next
        
# travlinkelist(a)


# recursive traversal

def rectravel(head):
    # base case
    if head is None:
        return
    print("->".join(head.val))
    rectravel(head.next)
    
rectravel(a)
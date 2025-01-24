class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def build_linked_list(nodes):
    if not nodes:
        return None

    node_objects = [Node(val) for val, _ in nodes]

    for index, (val, random_index) in enumerate(nodes):
        if index + 1 < len(node_objects):
            node_objects[index].next = node_objects[index + 1]
        if random_index is not None:
            node_objects[index].random = node_objects[random_index]

    return node_objects[0]

def copyRandomList(head):
    if not head:
        return None

    oldtoCopy = {}
    curr = head

    # First pass: create copies of each node
    while curr:
        copy = Node(curr.val)
        oldtoCopy[curr] = copy
        print(oldtoCopy)
        curr = curr.next

    # Second pass: assign next and random pointers
    curr = head
    while curr:
        oldtoCopy[curr].next = oldtoCopy.get(curr.next)
        oldtoCopy[curr].random = oldtoCopy.get(curr.random)
        curr = curr.next

    return oldtoCopy[head]

# Input list: [value, random_pointer_index]
head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

linked_list_head = build_linked_list(head)
copied_list = copyRandomList(linked_list_head)
class Node:
    """Class to represent a node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Class to represent a linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """Display all nodes in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def count_nodes(llist):
    """Count the total number of nodes in the linked list."""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# Test the implementation
llist = LinkedList()
for i in range(5):
    llist.append(i)

print("Linked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")

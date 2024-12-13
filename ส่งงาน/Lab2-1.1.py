class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def exercise1():
    # Create a new Linked List
    llist = LinkedList()

    # Append data
    print("1. Append data 1, 2, 3 to the end of the list")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("Result:")
    llist.display()

    # Prepend data
    print("\n2. Prepend data 0 to the start of the list")
    llist.prepend(0)
    print("Result:")
    llist.display()

    # Delete data
    print("\n3. Delete data 2")
    llist.delete(2)
    print("Result:")
    llist.display()

# Run the exercise
exercise1()


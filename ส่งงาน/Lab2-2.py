class Node:
    """Class to represent a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the new node
            new_node.prev = current  # Set the previous link for the new node

    def display_forward(self):
        """Display all nodes in the list from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display all nodes in the list from tail to head."""
        current = self.head
        if not current:  # If the list is empty
            print("None")
            return
        while current.next:  # Traverse to the end of the list
            current = current.next
        while current:  # Traverse backward to the head
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# ทดสอบการใช้งาน Doubly Linked List
dll = DoublyLinkedList()

# ให้ผู้ใช้กรอกเลขเอง
print("กรอกตัวเลขสำหรับเพิ่มใน Doubly Linked List (พิมพ์ 'exit' เพื่อหยุด):")
while True:
    user_input = input("กรอกตัวเลข: ")
    if user_input.lower() == 'exit':
        break
    try:
        number = int(user_input)
        dll.append(number)
    except ValueError:
        print("กรุณากรอกตัวเลขที่ถูกต้อง!")

print("\nแสดง Doubly Linked List จากหัวไปท้าย:")
dll.display_forward()

print("แสดง Doubly Linked List จากท้ายไปหัว:")
dll.display_backward()

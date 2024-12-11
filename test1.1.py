
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        prev = None
        if current is not None and current.data == data:
            self.head = current.next
            current = None
            return
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# สร้าง Linked List
llist = LinkedList()

# เพิ่มข้อมูล
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)

# ลบข้อมูล
llist.delete(2)

# แสดงผลลัพธ์
llist.display()
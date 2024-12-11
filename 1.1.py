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
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# สร้าง Linked List ใหม่
llist = LinkedList()

# เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List
print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
llist.append(1)
llist.append(2)
llist.append(3)
print("ผลลัพธ์:")
llist.display()

# เพิ่มข้อมูล 0 ที่หน้า List
print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
llist.prepend(0)
print("ผลลัพธ์:")
llist.display()

# ลบข้อมูล 2
print("\n3. ลบข้อมูล 2")
llist.delete(2)
print("ผลลัพธ์:")
llist.display()
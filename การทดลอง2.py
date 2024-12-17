# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
# เพิ่มข้อมูลที่ท้ายลิสต์
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
# เพิ่มข้อมูลที่หัวลิสต์
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
# ลบข้อมูล
    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
        print(f"ไม่พบข้อมูล {key}")
# แสดงผลลิสต์
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
# ทดสอบการใช้งาน
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print("แสดงลิสต์หลังเพิ่มท้าย:")
dll.display()
dll.prepend(0)
print("แสดงลิสต์หลังเพิ่มหัว:")
dll.display()
dll.delete(2)
print("แสดงลิสต์หลังลบข้อมูล 2:")
dll.display()

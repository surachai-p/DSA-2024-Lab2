class Node:
    """โครงสร้างของ Node ใน Doubly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """โครงสร้าง Doubly Linked List"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """เพิ่ม Node ที่ท้าย Doubly Linked List"""
        new_node = Node(data)
        if not self.head:  # ถ้า Linked List ว่าง
            self.head = new_node
            return
        current = self.head
        while current.next:  # หา Node ท้ายสุด
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        """เพิ่ม Node ที่หัว Doubly Linked List"""
        new_node = Node(data)
        if not self.head:  # ถ้า Linked List ว่าง
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """แสดงข้อมูลใน Doubly Linked List"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        """แสดงข้อมูลใน Doubly Linked List แบบย้อนกลับ"""
        if not self.head:
            print("None")
            return
        current = self.head
        while current.next:  # หา Node สุดท้าย
            current = current.next
        while current:  # แสดงข้อมูลย้อนกลับ
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# ทดสอบการใช้งาน Doubly Linked List
dll = DoublyLinkedList()

# เพิ่มข้อมูลที่ท้าย
dll.append(1)
dll.append(2)
dll.append(3)
print("แสดงข้อมูลจากหัวไปท้าย:")
dll.display()

# เพิ่มข้อมูลที่หน้า
dll.prepend(0)
print("\nแสดงข้อมูลจากหัวไปท้ายหลังเพิ่ม 0 ที่หัว:")
dll.display()

# แสดงข้อมูลย้อนกลับ
print("\nแสดงข้อมูลจากท้ายไปหัว:")
dll.display_reverse()

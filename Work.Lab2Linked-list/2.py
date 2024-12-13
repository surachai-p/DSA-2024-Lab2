class Node:
    def __init__(self, value):
        self.value = value  # เก็บค่าของจำนวนนักศึกษา
        self.prev = None    # ชี้ไปที่ Node ก่อนหน้า
        self.next = None    # ชี้ไปที่ Node ถัดไป

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # จุดเริ่มต้นของ Linked List
        self.tail = None  # จุดสิ้นสุดของ Linked List

    def add(self, value):
        new_node = Node(value)
        if not self.head:  # ถ้ายังไม่มี Node ใน Linked List
            self.head = self.tail = new_node
        else:  # เพิ่ม Node ใหม่ที่ท้าย Linked List
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# ใช้งาน
dll = DoublyLinkedList()
dll.add(50)  # เพิ่มจำนวนนักศึกษา 50 คน
dll.add(75)  # เพิ่มจำนวนนักศึกษา 75 คน
dll.add(100) # เพิ่มจำนวนนักศึกษา 100 คน

print("จำนวนนักศึกษาที่บันทึกไว้:")
dll.display()  # แสดงจำนวนนักศึกษาใน Linked List

print(f"จำนวนนักศึกษาทั้งหมด: {dll.count()} คน")


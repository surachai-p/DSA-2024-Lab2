class Node:
    def __init__(self, data):
        self.data = data           # เก็บข้อมูลของ Node
        self.next = None           # ชี้ไป Node ถัดไป
        self.prev = None           # ชี้ไป Node ก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None           # กำหนด head เริ่มต้นเป็น None (List ว่าง)
        
    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Doubly Linked List"""
        new_node = Node(data)
        if not self.head:          # กรณี List ว่าง
            self.head = new_node
            return
        current = self.head
        while current.next:        # ไปยัง Node สุดท้าย
            current = current.next
        current.next = new_node    # เพิ่ม Node ใหม่ที่ท้าย
        new_node.prev = current    # ชี้กลับไปยัง Node ก่อนหน้า

    def prepend(self, data):
        """เพิ่มข้อมูลที่หน้า Doubly Linked List"""
        new_node = Node(data)
        if self.head:              # ถ้ามี Node อยู่แล้ว
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node       # กำหนดให้ Node ใหม่เป็นหัว
    
    def delete(self, key):
        """ลบข้อมูลออกจาก Doubly Linked List"""
        current = self.head

        # ค้นหาและลบ Node
        while current:
            if current.data == key:
                if current.prev:   # มี Node ก่อนหน้า
                    current.prev.next = current.next
                else:              # ลบ Node แรก
                    self.head = current.next
                if current.next:   # มี Node ถัดไป
                    current.next.prev = current.prev
                return
            current = current.next
    
    def display(self):
        """แสดงข้อมูลทั้งหมดจากซ้ายไปขวา"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def search(self, key):
        """ค้นหาข้อมูลใน Doubly Linked List"""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

def exercise2():
    # สร้าง Doubly Linked List ใหม่
    dlist = DoublyLinkedList()
    
    # เพิ่มข้อมูล
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    print("ผลลัพธ์:")
    dlist.display()
    
    # เพิ่มข้อมูลที่หน้า List
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    dlist.prepend(0)
    print("ผลลัพธ์:")
    dlist.display()
    
    # ลบข้อมูล
    print("\n3. ลบข้อมูล 2")
    dlist.delete(2)
    print("ผลลัพธ์:")
    dlist.display()
    
    # ค้นหาข้อมูล
    print("\n4. ค้นหาข้อมูล 3 ใน List")
    position = dlist.search(3)
    if position != -1:
        print(f"พบข้อมูล 3 ที่ตำแหน่ง: {position}")
    else:
        print("ไม่พบข้อมูล 3")

exercise2()

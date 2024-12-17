import os

class Node:
    """โครงสร้างของ Node ใน Doubly Linked List"""
    def __init__(self, data):
        self.data = data  # ข้อมูลใน Node
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป
        self.prev = None  # ตัวชี้ไปยัง Node ก่อนหน้า

class DoublyLinkedList:
    """โครงสร้างของ Doubly Linked List"""
    def __init__(self):
        self.head = None  # หัวของ Doubly Linked List
        self.tail = None  # ท้ายของ Doubly Linked List

    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Doubly Linked List"""
        new_node = Node(data)
        if not self.head:  # กรณี Doubly Linked List ว่างเปล่า
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """เพิ่มข้อมูลที่หน้า Doubly Linked List"""
        new_node = Node(data)
        if not self.head:  # กรณี Doubly Linked List ว่างเปล่า
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, key):
        """ลบ Node ที่มีข้อมูลตรงกับ key"""
        current = self.head
        while current:
            if current.data == key:
                if current == self.head:  # ลบ Node หัว
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:  # ลบ Node ท้าย
                    self.tail = current.prev
                    self.tail.next = None
                else:  # ลบ Node กลาง
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # จบการทำงานหลังจากลบสำเร็จ
            current = current.next
        print(f"ไม่พบข้อมูล {key} ใน Doubly Linked List")

    def display_forward(self):
        """แสดงข้อมูลจากหัวไปท้าย Doubly Linked List"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """แสดงข้อมูลจากท้ายกลับไปหัว Doubly Linked List"""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def clear_screen():
    """เคลียร์หน้าจอคอนโซลตาม OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

# ตัวอย่างการใช้งาน
def exercise2():
    dll = DoublyLinkedList()

    while True:
        print("\n===== Doubly Linked List Menu =====")
        print("1. เพิ่มข้อมูลที่ท้าย Doubly Linked List")
        print("2. เพิ่มข้อมูลที่หน้า Doubly Linked List")
        print("3. ลบข้อมูล")
        print("4. แสดงข้อมูลจากหัวไปท้าย")
        print("5. แสดงข้อมูลจากท้ายกลับไปหัว")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกคำสั่ง (1-6): ")
        clear_screen()
        
        if choice == '1':
            data = input("ป้อนข้อมูลที่ต้องการเพิ่มท้าย: ")
            dll.append(data)
            print("\nผลลัพธ์ (แสดงไปข้างหน้า):")
            dll.display_forward()
        elif choice == '2':
            data = input("ป้อนข้อมูลที่ต้องการเพิ่มหน้า: ")
            dll.prepend(data)
            print("\nผลลัพธ์ (แสดงไปข้างหน้า):")
            dll.display_forward()
        elif choice == '3':
            data = input("ป้อนข้อมูลที่ต้องการลบ: ")
            dll.delete(data)
            print("\nผลลัพธ์ (แสดงไปข้างหน้า):")
            dll.display_forward()
        elif choice == '4':
            print("\nแสดงข้อมูลจากหัวไปท้าย:")
            dll.display_forward()
        elif choice == '5':
            print("\nแสดงข้อมูลจากท้ายกลับไปหัว:")
            dll.display_backward()
        elif choice == '6':
            print("\nจบการทำงานโปรแกรม")
            break
        else:
            print("\nกรุณาเลือกคำสั่งให้ถูกต้อง (1-6)")

# ทดสอบฟังก์ชัน
exercise2()

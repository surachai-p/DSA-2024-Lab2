# ประกาศคลาส Node
class Node:
    def __init__(self, data):
        self.data = data  # กำหนดข้อมูล
        self.next = None  # กำหนดตัวชี้ไปยังโหนดถัดไป

# ประกาศคลาส LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # เริ่มต้นด้วยหัวข้อว่าง

    # เพิ่มข้อมูลที่ท้าย List
    def append(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        if not self.head:  # ถ้า LinkedList ว่าง
            self.head = new_node  # กำหนดโหนดใหม่เป็นหัว
            return
        last_node = self.head
        while last_node.next:  # หาท้ายของ List
            last_node = last_node.next
        last_node.next = new_node  # เชื่อมโหนดใหม่เข้าที่ท้าย

    # เพิ่มข้อมูลที่หน้า List
    def prepend(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        new_node.next = self.head  # เชื่อมโหนดใหม่กับหัวเดิม
        self.head = new_node  # กำหนดโหนดใหม่เป็นหัว

    # ลบข้อมูล
    def delete(self, data):
        current = self.head
        if current and current.data == data:  # ถ้าเป็นโหนดแรก
            self.head = current.next  # ลบหัวและชี้ไปยังโหนดถัดไป
            current = None
            return
        prev = None
        while current and current.data != data:  # ค้นหาโหนดที่จะลบ
            prev = current
            current = current.next
        if current is None:  # ถ้าไม่พบข้อมูล
            print(f"ข้อมูล {data} ไม่พบใน Linked List")
            return
        prev.next = current.next  # ลบโหนดโดยเชื่อมโยงโหนดก่อนหน้ากับโหนดถัดไป
        current = None

    # แสดงผลข้อมูลใน Linked List
    def display(self):
        current = self.head
        if not current:
            print("Linked List ว่าง")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # จบด้วย None เพื่อบ่งบอกจุดสิ้นสุดของ List

# ฟังก์ชัน exercise1
def exercise1():
    # สร้าง Linked List ใหม่
    llist = LinkedList()
    
    # เพิ่มข้อมูล
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("ผลลัพธ์:")
    llist.display()
    
    # เพิ่มข้อมูลที่หน้า List
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    llist.prepend(0)
    print("ผลลัพธ์:")
    llist.display()
    
    # ลบข้อมูล
    print("\n3. ลบข้อมูล 2")
    llist.delete(2)
    print("ผลลัพธ์:")
    llist.display()

# เรียกใช้ฟังก์ชัน exercise1
exercise1()


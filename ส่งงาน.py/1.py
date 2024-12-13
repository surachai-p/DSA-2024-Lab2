class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลที่เก็บใน Node
        self.next = None  # ตัวเชื่อมไปยัง Node ถัดไป

class LinkedList:
    def __init__(self):
        self.head = None  # หัวของ Linked List

    # เพิ่มข้อมูลที่ท้ายของ Linked List
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # ถ้า Linked List ว่างให้ตั้งหัวเป็น Node ใหม่
        else:
            last = self.head
            while last.next:  # หาตำแหน่งสุดท้าย
                last = last.next
            last.next = new_node  # เชื่อม Node ใหม่เข้ากับท้ายสุด

    # เพิ่มข้อมูลที่หน้า (ก่อนหน้า) ของ Linked List
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Node ใหม่จะเชื่อมกับหัวเดิม
        self.head = new_node  # ตั้งหัวใหม่เป็น Node ใหม่

    # ลบข้อมูลใน Linked List ตามค่าที่กำหนด
    def delete(self, data):
        current = self.head
        previous = None
        
        # ถ้าหัวเป็น Node ที่จะลบ
        if current and current.data == data:
            self.head = current.next  # ให้หัวไปชี้ Node ถัดไป
            current = None  # ลบ Node เดิม
            return

        # หา Node ที่ต้องการลบ
        while current and current.data != data:
            previous = current
            current = current.next

        # ถ้าหา Node ไม่พบ
        if not current:
            print(f"ไม่พบข้อมูล {data} ใน Linked List")
            return

        # ลบ Node ที่เจอ
        previous.next = current.next
        current = None

    # แสดงข้อมูลทั้งหมดใน Linked List
    def display(self):
        current = self.head
        if not current:
            print("Linked List ว่าง")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # แสดงท้ายสุดว่าไม่มี Node ถัดไป

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

# เรียกใช้งานฟังก์ชัน exercise1
exercise1()

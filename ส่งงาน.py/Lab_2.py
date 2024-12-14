class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลในโหนด
        self.next = None  # ตัวชี้ไปยังโหนดถัดไป
        self.prev = None  # ตัวชี้ไปยังโหนดก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # เริ่มต้นด้วยหัวว่าง

    # เพิ่มข้อมูลที่ท้ายของลิสต์
    def append(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        if not self.head:  # ถ้าลิสต์ว่าง
            self.head = new_node  # กำหนดโหนดใหม่เป็นหัว
            return
        last_node = self.head
        while last_node.next:  # ค้นหาท้ายลิสต์
            last_node = last_node.next
        last_node.next = new_node  # เชื่อมโหนดใหม่ที่ท้าย
        new_node.prev = last_node  # เชื่อมย้อนกลับไปยังโหนดก่อนหน้า

    # เพิ่มข้อมูลที่หน้า (เช่น การแทรกข้อมูลที่หัว)
    def prepend(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        if not self.head:  # ถ้าลิสต์ว่าง
            self.head = new_node  # กำหนดโหนดใหม่เป็นหัว
            return
        new_node.next = self.head  # เชื่อมไปยังโหนดที่หัว
        self.head.prev = new_node  # เชื่อมย้อนกลับไปยังโหนดใหม่
        self.head = new_node  # กำหนดโหนดใหม่เป็นหัว

    # ลบข้อมูลจากลิสต์
    def delete(self, data):
        current = self.head
        if current and current.data == data:  # ถ้าเป็นโหนดแรก
            if current.next:  # ถ้ามีโหนดถัดไป
                current.next.prev = None  # เชื่อมย้อนกลับ
            self.head = current.next  # กำหนดหัวใหม่
            current = None
            return
        while current:  # ค้นหาโหนดที่ต้องการลบ
            if current.data == data:
                if current.next:  # ถ้ามีโหนดถัดไป
                    current.next.prev = current.prev  # เชื่อมไปยังโหนดก่อนหน้า
                if current.prev:  # ถ้ามีโหนดก่อนหน้า
                    current.prev.next = current.next  # เชื่อมไปยังโหนดถัดไป
                current = None
                return
            current = current.next
        print(f"ข้อมูล {data} ไม่พบใน Doubly Linked List")

    # แสดงผลข้อมูลในลิสต์
    def display(self):
        current = self.head
        if not current:
            print("Doubly Linked List ว่าง")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# ทดสอบการใช้งาน Doubly Linked List
dllist = DoublyLinkedList()
dllist.append(10)
dllist.append(20)
dllist.append(30)

print("Doubly Linked List:")
dllist.display()

dllist.prepend(5)
print("\nหลังจากเพิ่มข้อมูลที่หน้า:")
dllist.display()

dllist.delete(20)
print("\nหลังจากลบข้อมูล 20:")
dllist.display()

dllist.delete(5)
print("\nหลังจากลบข้อมูล 5:")
dllist.display()

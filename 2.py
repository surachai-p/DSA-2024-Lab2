class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # ชี้ไปที่โหนดถัดไป
        self.prev = None  # ชี้ไปที่โหนดก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # เริ่มต้นด้วย head เป็น None

    # ฟังก์ชันเพิ่มข้อมูลที่ท้าย List
    def append(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        if not self.head:  # ถ้า List ว่าง
            self.head = new_node
        else:
            last = self.head
            while last.next:  # เดินไปจนถึงโหนดสุดท้าย
                last = last.next
            last.next = new_node  # เชื่อมโยงโหนดใหม่กับโหนดสุดท้าย
            new_node.prev = last  # ตั้งค่าผลย้อนกลับไปยังโหนดก่อนหน้า

    # ฟังก์ชันเพิ่มข้อมูลที่หน้า List
    def prepend(self, data):
        new_node = Node(data)  # สร้างโหนดใหม่
        if not self.head:  # ถ้า List ว่าง
            self.head = new_node
        else:
            new_node.next = self.head  # เชื่อมโยงโหนดใหม่กับโหนดแรก
            self.head.prev = new_node  # ตั้งค่าผลย้อนกลับไปยังโหนดใหม่
            self.head = new_node  # ตั้งให้โหนดใหม่เป็น head

    # ฟังก์ชันลบข้อมูล
    def delete(self, data):
        current = self.head
        while current:  # เดินไปยังทุกโหนด
            if current.data == data:  # ถ้าหาเจอข้อมูลที่ต้องการลบ
                if current.prev:  # ถ้ามีโหนดก่อนหน้า
                    current.prev.next = current.next  # เชื่อมโยงโหนดก่อนหน้ากับโหนดถัดไป
                if current.next:  # ถ้ามีโหนดถัดไป
                    current.next.prev = current.prev  # เชื่อมโยงโหนดถัดไปกลับมายังโหนดก่อนหน้า
                if current == self.head:  # ถ้าเป็นโหนดแรก
                    self.head = current.next  # ตั้งให้โหนดถัดไปเป็น head
                current = None  # ลบโหนดออก
                return
            current = current.next  # ไปยังโหนดถัดไป

    # ฟังก์ชันแสดงข้อมูลจากหน้าไปหลัง
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # ฟังก์ชันแสดงข้อมูลจากหลังไปหน้า
    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next  # ไปยังโหนดสุดท้าย
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# ทดสอบการใช้งาน Doubly Linked List
def test_doubly_linked_list():
    dll = DoublyLinkedList()

    # เพิ่มข้อมูลที่ท้าย
    print("เพิ่มข้อมูลที่ท้าย List:")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display_forward()  # แสดงข้อมูลจากหน้าไปหลัง

    # เพิ่มข้อมูลที่หน้า
    print("\nเพิ่มข้อมูลที่หน้า List:")
    dll.prepend(5)
    dll.prepend(0)
    dll.display_forward()  # แสดงข้อมูลจากหน้าไปหลัง

    # ลบข้อมูล
    print("\nลบข้อมูล 20:")
    dll.delete(20)
    dll.display_forward()  # แสดงข้อมูลจากหน้าไปหลัง

    print("\nแสดงข้อมูลจากหลังไปหน้า:")
    dll.display_backward()  # แสดงข้อมูลจากหลังไปหน้า

# เรียกใช้งาน
test_doubly_linked_list()

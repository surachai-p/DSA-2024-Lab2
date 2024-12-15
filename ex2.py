# สร้างคลาสสำหรับ Node
class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลที่เก็บ
        self.prev = None  # ชี้ไปยัง Node ก่อนหน้า
        self.next = None  # ชี้ไปยัง Node ถัดไป

# สร้างคลาสสำหรับ Doubly Linked-List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # ตัวชี้ไปยังหัวของลิสต์

    # ฟังก์ชันสำหรับเพิ่มข้อมูลที่หัวของลิสต์
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  # ถ้าลิสต์ว่าง
            self.head = new_node
        else:
            new_node.next = self.head  # ชี้ไปยัง Node ถัดไป
            self.head.prev = new_node  # ชี้กลับไปยัง Node ก่อนหน้า
            self.head = new_node  # เปลี่ยนหัวลิสต์เป็น Node ใหม่

    # ฟังก์ชันสำหรับเพิ่มข้อมูลที่ท้ายของลิสต์
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # ถ้าลิสต์ว่าง
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:  # ค้นหาท้ายของลิสต์
                last_node = last_node.next
            last_node.next = new_node  # เชื่อม Node ใหม่
            new_node.prev = last_node  # ชี้กลับไปยัง Node ก่อนหน้า

    # ฟังก์ชันสำหรับลบ Node ที่มีข้อมูล
    def delete(self, data):
        current_node = self.head
        while current_node:  # หา Node ที่มีข้อมูลตรงกับที่ต้องการลบ
            if current_node.data == data:
                if current_node.prev:  # ถ้ามี Node ก่อนหน้า
                    current_node.prev.next = current_node.next
                if current_node.next:  # ถ้ามี Node ถัดไป
                    current_node.next.prev = current_node.prev
                if current_node == self.head:  # ถ้าเป็น Node ที่หัว
                    self.head = current_node.next
                current_node = None
                return
            current_node = current_node.next

    # ฟังก์ชันสำหรับแสดงผลลิสต์จากหัวไปหาง
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")  # แสดงท้ายลิสต์

    # ฟังก์ชันสำหรับแสดงผลลิสต์จากหางไปหัว
    def display_reverse(self):
        current_node = self.head
        if not current_node:
            return
        # ไปยัง Node ท้ายสุดก่อน
        while current_node.next:
            current_node = current_node.next
        # แสดงผลจากท้ายไปหัว
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")  # แสดงท้ายลิสต์

# ทดสอบการใช้งาน Doubly Linked-List
dll = DoublyLinkedList()

# เพิ่มข้อมูล
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

# แสดงผลลิสต์จากหัวไปหาง
dll.display()

# แสดงผลลิสต์จากหางไปหัว
dll.display_reverse()

# ลบข้อมูล
dll.delete(20)

# แสดงผลลิสต์หลังการลบ
dll.display()

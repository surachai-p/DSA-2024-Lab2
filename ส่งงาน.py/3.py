class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลใน Node
        self.next = None  # ตัวเชื่อมไปยัง Node ถัดไป
        self.prev = None  # ตัวเชื่อมไปยัง Node ก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # หัวของ Doubly Linked List

    # เพิ่มข้อมูลที่ท้ายของ Doubly Linked List
    def append(self, data):
        new_node = Node(data)  # สร้าง Node ใหม่
        if not self.head:  # ถ้า Linked List ว่าง
            self.head = new_node
        else:
            current = self.head
            while current.next:  # ไปหาตำแหน่งท้ายสุด
                current = current.next
            current.next = new_node  # เชื่อม Node ใหม่ไปยังท้ายสุด
            new_node.prev = current  # เชื่อม Node ใหม่กลับไปยัง Node ก่อนหน้า

    # แสดงข้อมูลทั้งหมดจากหน้าไปหลัง (Forward Traversal)
    def display_forward(self):
        current = self.head
        if not current:
            print("Doubly Linked List ว่าง")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # แสดงท้ายสุดว่าไม่มี Node ถัดไป

    # แสดงข้อมูลทั้งหมดจากหลังไปหน้า (Backward Traversal)
    def display_backward(self):
        current = self.head
        if not current:
            print("Doubly Linked List ว่าง")
            return

        # ไปยัง Node ท้ายสุดก่อน
        while current.next:
            current = current.next
        
        # แสดงข้อมูลจากหลังไปหน้า
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    # ลบข้อมูลจากท้ายของ Doubly Linked List
    def delete_last(self):
        if not self.head:  # ถ้า Linked List ว่าง
            print("Doubly Linked List ว่าง")
            return
        current = self.head
        while current.next:  # ไปหาตำแหน่งท้ายสุด
            current = current.next
        if current.prev:  # ถ้ามี Node ก่อนหน้า
            current.prev.next = None
        else:
            self.head = None  # ถ้าเป็น Node แรกก็ทำให้ head เป็น None
        print(f"Deleted node with data: {current.data}")

    # ลบข้อมูลที่มีค่าเท่ากับ data
    def delete_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:  # ถ้ามี Node ก่อนหน้า
                    current.prev.next = current.next
                if current.next:  # ถ้ามี Node ถัดไป
                    current.next.prev = current.prev
                if current == self.head:  # ถ้าคือ Node แรก
                    self.head = current.next
                print(f"Deleted node with data: {current.data}")
                return
            current = current.next
        print(f"ไม่พบข้อมูล {data} ใน Doubly Linked List")

# ทดสอบการใช้งาน
dll = DoublyLinkedList()

# เพิ่มข้อมูล
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

# แสดงข้อมูลจากหน้าไปหลัง
print("Display Forward:")
dll.display_forward()

# แสดงข้อมูลจากหลังไปหน้า
print("\nDisplay Backward:")
dll.display_backward()

# ลบข้อมูลจากท้ายสุด
dll.delete_last()
print("\nหลังจากลบท้ายสุด:")
dll.display_forward()

# ลบข้อมูลที่มีค่าเท่ากับ 20
dll.delete_data(20)
print("\nหลังจากลบข้อมูลที่มีค่า 20:")
dll.display_forward()

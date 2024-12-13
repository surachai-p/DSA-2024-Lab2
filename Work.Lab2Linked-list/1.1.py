# โครงสร้างของ Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# โครงสร้างของ Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # เพิ่มข้อมูลที่ท้าย List
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # เพิ่มข้อมูลที่หน้า List
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ลบข้อมูลใน List
    def delete(self, key):
        current = self.head

        # ถ้าข้อมูลที่จะลบอยู่ที่หัว List
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # ค้นหาข้อมูลที่จะลบ
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # ถ้าไม่พบข้อมูลใน List
        if current is None:
            print(f"ไม่พบข้อมูล {key} ใน List")
            return

        # ลบ Node ออกจาก List
        prev.next = current.next
        current = None

    # แสดงข้อมูลใน List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


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

# เรียกใช้งานแบบฝึกหัดที่ 1
exercise1()



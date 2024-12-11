class Node:
    def __init__(self, data):
        self.data = data  # เก็บข้อมูลของ Node
        self.next = None  # pointer ชี้ไป Node ถัดไป

class LinkedList:
    def __init__(self):
        self.head = None  # กำหนด head เริ่มต้นเป็น None (List ว่าง)

    def append(self, data):
        # เพิ่มข้อมูลที่ท้าย Linked List
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        # เพิ่มข้อมูลที่หน้า Linked List
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        # ลบข้อมูลที่ต้องการออกจาก List
        current = self.head

        # กรณีลบ Node แรก
        if current and current.data == key:
            self.head = current.next
            return

        # กรณีลบ Node อื่นๆ
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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

def count_nodes(llist):
    """นับจำนวน Node ทั้งหมด"""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# ทดสอบการใช้งาน
llist = LinkedList()
for i in range(5):
    llist.append(i)

print("Linked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")

class Node:
    def __init__(self, data):
        self.data = data  # กำหนดข้อมูล
        self.next = None  # กำหนดตัวชี้ไปยังโหนดถัดไป

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

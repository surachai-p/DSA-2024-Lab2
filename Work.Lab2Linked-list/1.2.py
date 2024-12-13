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

    # แสดงข้อมูลใน List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ฟังก์ชันนับจำนวน Node
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

# เพิ่มข้อมูลเข้า Linked List
for i in range(5):
    llist.append(i)

# แสดง Linked List
print("Linked List ที่สร้าง:")
llist.display()

# นับจำนวน Node และแสดงผล
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")

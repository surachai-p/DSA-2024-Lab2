class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลใน Node
        self.next = None  # ตัวเชื่อมไปยัง Node ถัดไป

class LinkedList:
    def __init__(self):
        self.head = None  # หัวของ Linked List

    # เพิ่มข้อมูลที่ท้ายของ Linked List
    def append(self, data):
        new_node = Node(data)  # สร้าง Node ใหม่
        if not self.head:  # ถ้า Linked List ว่าง
            self.head = new_node
        else:
            current = self.head
            while current.next:  # ไปหาตำแหน่งท้ายสุด
                current = current.next
            current.next = new_node  # เชื่อม Node ใหม่ไปยังท้ายสุด

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

# ฟังก์ชันนับจำนวน Node ทั้งหมด
def count_nodes(llist):
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# ทดสอบการใช้งาน
llist = LinkedList()
for i in range(5):  # เพิ่มข้อมูล 0 ถึง 4
    llist.append(i)

# แสดง Linked List และจำนวน Node
print("Linked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")

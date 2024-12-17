class Node:
    """โครงสร้างของ Node ใน Linked List"""
    def __init__(self, data):
        self.data = data  # ข้อมูลใน Node
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป

class LinkedList:
    """โครงสร้างของ Linked List"""
    def __init__(self):
        self.head = None  # หัวของ Linked List

    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Linked List โดยใช้ recursive"""
        def _append(node, data):
            if not node.next:  # หากถึง Node สุดท้าย
                node.next = Node(data)
            else:
                _append(node.next, data)

        if not self.head:  # กรณี Linked List ว่างเปล่า
            self.head = Node(data)
        else:
            _append(self.head, data)

    def prepend(self, data):
        """เพิ่มข้อมูลที่หน้า Linked List"""
        new_node = Node(data)  # สร้าง Node ใหม่
        new_node.next = self.head  # ชี้ไปยัง Node เดิมที่เป็นหัว
        self.head = new_node  # ตั้ง Node ใหม่เป็นหัวของ Linked List

    def delete(self, key):
        """ลบข้อมูลที่มีค่าเท่ากับ key โดยใช้ recursive"""
        def _delete(node, key):
            if not node:
                return None
            if node.data == key:  # พบ Node ที่ต้องการลบ
                return node.next
            node.next = _delete(node.next, key)
            return node

        self.head = _delete(self.head, key)

    def display(self):
        """แสดงข้อมูลใน Linked List โดยใช้ recursive"""
        def _display(node):
            if not node:
                print("None")
                return
            print(node.data, end=" -> ")
            _display(node.next)

        _display(self.head)

def count_nodes(llist):
    """นับจำนวน Node ทั้งหมด"""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# ตัวอย่างการเรียกใช้งาน
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

    # นับจำนวน Node
    print("\n4. นับจำนวน Node ทั้งหมด")
    print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")

# ทดสอบฟังก์ชัน
exercise1()

# ทดสอบการใช้งานเพิ่มเติม
llist = LinkedList()
for i in range(5):
    llist.append(i)

print("\nLinked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def prepend(self, data):
        """เพิ่มข้อมูลที่หน้า Linked List"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """ลบข้อมูลที่ต้องการออกจาก List"""
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
        """แสดงข้อมูลทั้งหมดใน List"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        """ค้นหาข้อมูลใน List"""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

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
    
exercise1()

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

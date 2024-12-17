class Node:
    def __init__(self, data):
        self.data = data        # เก็บข้อมูลของ Node
        self.next = None        # pointer ไปยัง Node ถัดไป
        self.prev = None        # pointer ไปยัง Node ก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # หัวของ List เริ่มต้นเป็น None

    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Doubly Linked List"""
        new_node = Node(data)
        if not self.head:       # ถ้า List ว่าง
            self.head = new_node
            return
        current = self.head
        while current.next:     # ไปยัง Node สุดท้าย
            current = current.next
        current.next = new_node
        new_node.prev = current # ชี้ย้อนกลับไปยัง Node ก่อนหน้า

    def prepend(self, data):
        """เพิ่มข้อมูลที่หน้า Doubly Linked List"""
        new_node = Node(data)
        if self.head:           # ถ้ามี Node อยู่แล้ว
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node    # กำหนดหัวใหม่

    def delete(self, key):
        """ลบข้อมูลที่ต้องการออกจาก Doubly Linked List"""
        current = self.head

        while current:
            if current.data == key:
                # กรณีเป็น Node แรก
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # กรณีเป็น Node ตรงกลางหรือท้าย
                else:
                    if current.next:
                        current.next.prev = current.prev
                    current.prev.next = current.next
                return
            current = current.next

    def display(self):
        """แสดงข้อมูลทั้งหมดใน Doubly Linked List"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def search(self, key):
        """ค้นหาข้อมูลใน Doubly Linked List"""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

def count_nodes(dlist):
    """นับจำนวน Node ทั้งหมดใน Doubly Linked List"""
    count = 0
    current = dlist.head
    while current:
        count += 1
        current = current.next
    return count

# ทดสอบการทำงาน
if __name__ == "__main__":
    dlist = DoublyLinkedList()
    
    # เพิ่มข้อมูลท้าย List
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    dlist.display()
    
    # เพิ่มข้อมูลที่หน้า List
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    dlist.prepend(0)
    dlist.display()

    # ลบข้อมูล
    print("\n3. ลบข้อมูล 2")
    dlist.delete(2)
    dlist.display()

    # ค้นหาข้อมูล
    print("\n4. ค้นหาข้อมูล 3 ใน List")
    position = dlist.search(3)
    if position != -1:
        print(f"พบข้อมูล 3 ที่ตำแหน่ง: {position}")
    else:
        print("ไม่พบข้อมูล 3")

    # นับจำนวน Node
    print("\n5. นับจำนวน Node ทั้งหมด")
    print(f"จำนวน Node ทั้งหมด: {count_nodes(dlist)}")

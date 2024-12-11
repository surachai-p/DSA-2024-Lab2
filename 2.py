class Node:
    """โครงสร้างของ Node ใน Doubly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """โครงสร้างของ Doubly Linked List"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """เพิ่มข้อมูลที่ท้าย Doubly Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        """เพิ่มข้อมูลที่หัว Doubly Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """ลบ Node ตามค่า"""
        current = self.head

        while current:
            if current.data == key:
                # กรณี Node เป็นหัว
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # กรณี Node อยู่ตรงกลางหรือท้าย
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                print(f"ลบข้อมูล {key} เรียบร้อยแล้ว")
                return
            current = current.next
        print(f"ไม่พบข้อมูล {key}")

    def count_nodes(self):
        """นับจำนวน Node ทั้งหมดใน Doubly Linked List"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, key):
        """ค้นหาข้อมูลใน Doubly Linked List"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """แสดงข้อมูลทั้งหมดใน Doubly Linked List"""
        current = self.head
        if not current:
            print("Doubly Linked List ว่างเปล่า")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# ฟังก์ชันหลักสำหรับทดสอบ Doubly Linked List
def main():
    dllist = DoublyLinkedList()

    while True:
        print("\nโปรดเลือกคำสั่ง:")
        print("1: เพิ่มข้อมูลที่ท้าย")
        print("2: เพิ่มข้อมูลที่หัว")
        print("3: ลบข้อมูล")
        print("4: นับจำนวนข้อมูลใน Doubly Linked List")
        print("5: ค้นหาข้อมูล")
        print("6: แสดงข้อมูลทั้งหมด")
        print("7: ออกจากโปรแกรม")

        choice = input("กรุณาเลือกคำสั่ง (1-7): ")

        if choice == '1':
            data = input("ป้อนข้อมูลที่ต้องการเพิ่มที่ท้าย: ")
            dllist.append(data)
            print(f"เพิ่มข้อมูล {data} ที่ท้ายเรียบร้อยแล้ว")

        elif choice == '2':
            data = input("ป้อนข้อมูลที่ต้องการเพิ่มที่หัว: ")
            dllist.prepend(data)
            print(f"เพิ่มข้อมูล {data} ที่หัวเรียบร้อยแล้ว")

        elif choice == '3':
            key = input("ป้อนข้อมูลที่ต้องการลบ: ")
            dllist.delete(key)

        elif choice == '4':
            count = dllist.count_nodes()
            print(f"จำนวน Node ทั้งหมดใน Doubly Linked List: {count}")

        elif choice == '5':
            key = input("ป้อนข้อมูลที่ต้องการค้นหา: ")
            if dllist.search(key):
                print(f"พบข้อมูล {key} ใน Doubly Linked List")
            else:
                print(f"ไม่พบข้อมูล {key}")

        elif choice == '6':
            print("ข้อมูลใน Doubly Linked List:")
            dllist.display()

        elif choice == '7':
            print("ออกจากโปรแกรม")
            break

        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้งานโปรแกรมหลัก
if __name__ == "__main__":
    main()

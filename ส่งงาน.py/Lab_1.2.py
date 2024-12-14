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

    def delete(self, data):
        """ลบข้อมูลตามค่าที่กำหนด"""
        if not self.head:
            print("List is empty.")
            return

        # ถ้าข้อมูลอยู่ที่หัว
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print(f"Data {data} not found in the list.")

    def display(self):
        """แสดงข้อมูลใน Linked List"""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ฟังก์ชันที่ให้มา

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

# เรียกใช้ฟังก์ชัน
def main():
    exercise1()

if __name__ == "__main__":
    main()

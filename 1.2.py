class Node:
    """โครงสร้างของ Node ใน Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """โครงสร้างของ Linked List"""
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

    def count_nodes(self):
        """นับจำนวน Node ทั้งหมดใน Linked List"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, key):
        """ค้นหาข้อมูลใน Linked List"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """แสดงข้อมูลทั้งหมดใน Linked List"""
        current = self.head
        if not current:
            print("Linked List ว่างเปล่า")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ฟังก์ชันหลักสำหรับทดสอบการนับและค้นหาข้อมูล
def main():
    llist = LinkedList()

    while True:
        print("\nโปรดเลือกคำสั่ง:")
        print("1: เพิ่มข้อมูล")
        print("2: นับจำนวนข้อมูลใน Linked List")
        print("3: ค้นหาข้อมูล")
        print("4: แสดงข้อมูลทั้งหมด")
        print("5: ออกจากโปรแกรม")

        choice = input("กรุณาเลือกคำสั่ง (1-5): ")

        if choice == '1':
            data = input("ป้อนข้อมูลที่ต้องการเพิ่ม: ")
            llist.append(data)
            print(f"เพิ่มข้อมูล {data} เรียบร้อยแล้ว")

        elif choice == '2':
            count = llist.count_nodes()
            print(f"จำนวน Node ทั้งหมดใน Linked List: {count}")

        elif choice == '3':
            key = input("ป้อนข้อมูลที่ต้องการค้นหา: ")
            if llist.search(key):
                print(f"พบข้อมูล {key} ใน Linked List")
            else:
                print(f"ไม่พบข้อมูล {key}")

        elif choice == '4':
            print("ข้อมูลใน Linked List:")
            llist.display()

        elif choice == '5':
            print("ออกจากโปรแกรม")
            break

        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้งานโปรแกรมหลัก
if __name__ == "__main__":
    main()

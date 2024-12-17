# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print(f"ไม่พบข้อมูล {key}")
            return
        prev.next = current.next
        current = None
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# ทดสอบการใช้งาน LinkedList
if __name__ == "__main__":
    llist = LinkedList()  
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.display()  
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    llist.prepend(0)
    llist.display()
    print("\n3. ลบข้อมูล 2")
    llist.delete(2)
    llist.display()


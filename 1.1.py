class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

def exercise1():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    llist.display()

    llist.prepend(0)
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    llist.display()

    llist.delete(2)
    print("\n3. ลบข้อมูล 2")
    llist.display()

exercise1()

##1.เขียนโปรแกรมเพื่อรัน แบบฝึกหัดที่ 1 และแบบฝึกหัดที่ 2
##แบบฝึกหัด 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
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
        if self.head is None:
            return
        
        #ลบอยู่ที่หัว
        if self.head.data == key:
            self.head = self.head.next
            return

        #ค้นหา ลบข้อมูล
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        
        if current.next:
            current.next = current.next.next

    #ส่วนLinked List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def exercise1():
    llist = LinkedList()
    
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List") #เพิ่มข้อมูล
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("ผลลัพธ์:")
    llist.display()
    
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    llist.prepend(0)
    print("ผลลัพธ์:")
    llist.display()   

    print("\n3. ลบข้อมูล 2") #ส่วนลบข้อมูล
    llist.delete(2)
    print("ผลลัพธ์:")
    llist.display()
exercise1()

##แบบฝึกหัดที่ 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """เพิ่มข้อมูลที่ท้ายของ Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """แสดงข้อมูลใน Linked List"""
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def count_nodes(llist):
    """นับจำนวน Node ทั้งหมดใน Linked List"""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

def exercise2():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)

    print("Linked List:")
    llist.display()

    print("\nจำนวน Node ทั้งหมดใน Linked List:", count_nodes(llist))
exercise2()
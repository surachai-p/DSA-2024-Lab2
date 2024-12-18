class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # ชี้ไปยัง Node แรกของ List

    def append(self, data):  # เพิ่มข้อมูลที่ท้าย List
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):  # เพิ่มข้อมูลที่หน้า List
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):  # พิมพ์ข้อมูลทั้งหมดใน List
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def delete_node(self, key):  # ลบ Node ที่มีข้อมูลตรงกับ key
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

def exercise2():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.prepend(0)
    llist.display()
    
    
    
exercise2()
### 2.จงเขียนโปรแกรมเพื่อสร้าง Doubly Linked-List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next

# สร้าง Doubly Linked List
dllist = DoublyLinkedList()

# เพิ่มข้อมูล
dllist.append(6)
dllist.append(8)
dllist.append(10)
dllist.prepend(4)

# พิมพ์ข้อมูลทั้งหมด
dllist.print_list()
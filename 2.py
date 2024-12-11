class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลที่เก็บไว้ในโหนด
        self.next = None  # ชี้ไปยังโหนดถัดไป
        self.prev = None  # ชี้ไปยังโหนดก่อนหน้า

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # เพิ่มโหนดที่ท้ายของลิสต์
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

    # เพิ่มโหนดที่ตำแหน่งใดๆ ในลิสต์
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    # ลบโหนดออกจากลิสต์
    def delete_node(self, data):
        if self.head is None:
            return
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            temp = None
            if self.head:
                self.head.prev = None
            return
        while temp is not None and temp.data != data:
            temp = temp.next
        if temp is None:
            return
        if temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        temp = None

    # พิมพ์ค่าของโหนดทั้งหมดในลิสต์
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
llist = DoublyLinkedList()
llist.append(6)
llist.append(4)
llist.append(8)
llist.insert_after(llist.head.next, 5)
llist.print_list()  # ผลลัพธ์: 6 4 5 8
llist.delete_node(4)
llist.print_list()  # ผลลัพธ์: 6 5 8
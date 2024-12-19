##2.จงเขียนโปรแกรมเพื่อสร้าง Doubly Linked-List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node
            new_node.prev = tail

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if current:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.head:  #ถ้าต้องการลบโหนดหัว
                self.head = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()  #10 <-> 20 <-> 30 <-> None

dll.prepend(5)
dll.display()  #5 <-> 10 <-> 20 <-> 30 <-> None

dll.delete(20)
dll.display()  #5 <-> 10 <-> 30 <-> None

dll.delete(5)
dll.display()  #10 <-> 30 <-> None

dll.delete(30)
dll.display()  #10 <-> None

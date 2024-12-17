
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
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                # ถ้า node นั้นไม่ใช่ node แรก
                if current.prev:
                    current.prev.next = current.next
                # ถ้า node นั้นไม่ใช่ node สุดท้าย
                if current.next:
                    current.next.prev = current.prev
                # ถ้า node ที่จะลบคือ node แรก
                if current == self.head:
                    self.head = current.next
                current = None  # ลบ node
            return
            current = current.next
    def count_nodes(llist):
        """นับจำนวน Node ทั้งหมด"""
        count = 0
        current = llist.head
        while current:
            count += 1
            current = current.next
        return count
    

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Doubly Linked List:")
dll.display()

dll.delete(20)
print("\nDoubly Linked List after deleting 20:")
dll.display()

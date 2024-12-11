##1.เขียนโปรแกรมเพื่อรันแบบฝึกหัดที่ 2
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        prev = None
        if current is not None and current.data == data:
            self.head = current.next
            current = None
            return
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# ทดสอบการใช้งาน
llist = LinkedList()
for i in range(5):
    llist.append(i)

print("Linked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {llist.count_nodes()}")

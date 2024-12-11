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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def count_nodes(llist):
    """นับจำนวน Node ทั้งหมด"""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# สร้าง Linked List
llist = LinkedList()
for i in range(5):
    llist.append(i)

# แสดง Linked List
print("Linked List ที่สร้าง:")
llist.display()

# นับจำนวน Node และแสดงผล
print(f"\nจำนวน Node ทั้งหมด: {count_nodes(llist)}")
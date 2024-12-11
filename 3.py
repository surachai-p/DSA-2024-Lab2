class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, student_id, name, grade):
        new_node = Node(student_id, name, grade)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_by_id(self, student_id):
        current_node = self.head
        prev_node = None
        while current_node and current_node.student_id != student_id:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("นักศึกษารหัสนี้ไม่พบ")
            return
        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

    def search_by_id(self, student_id):
        current_node = self.head
        while current_node and current_node.student_id != student_id:
            current_node = current_node.next
        if current_node is None:
            print("นักศึกษารหัสนี้ไม่พบ")
            return
        print(f"รหัส: {current_node.student_id}, ชื่อ: {current_node.name}, เกรด: {current_node.grade}")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"รหัส: {current_node.student_id}, ชื่อ: {current_node.name}, เกรด: {current_node.grade}")
            current_node = current_node.next

student_list = LinkedList()

# เพิ่มข้อมูลนักศึกษา
student_list.append(66030232, "ณัฏฐณิชชา กิติชยาโชติ", 4.00)
student_list.append(66030238, "ณัฐนันท์ สุวรรณโชติ", 3.88)
student_list.append(66030243, "ธัญเทพ หาญกล้า", 2.99)
student_list.append(66030284, "ศรสวรรค์ จันทสุววรณโณ", 3.45)
student_list.append(66030295, "สุวพัชร สระศรีสม", 3.00)


print("รายชื่อนักศึกษาทั้งหมด:")
student_list.print_list()

print("\nค้นหาข้อมูลนักศึกษารหัส 66030232:")
student_list.search_by_id(66030232)

print("\nลบข้อมูลนักศึกษารหัส 66030238")
student_list.delete_by_id(66030238)

# แสดงรายชื่อนักศึกษาทั้งหมดอีกครั้ง
print("\nรายชื่อนักศึกษาทั้งหมดหลังจากลบ:")
student_list.print_list()
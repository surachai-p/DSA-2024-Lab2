### 3.จงเขียนโปรแกรมใช้ Linked List ในการจัดการข้อมูลนักศึกษา โดยมีความสามารถดังนี้:
#1. เพิ่มข้อมูลนักศึกษา (รหัส, ชื่อ, เกรด) 
#2. ลบข้อมูลนักศึกษาตามรหัสนักศึกษา 
#3. ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา
#4. แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา
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

    def delete(self, student_id):
        current = self.head
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if current is None:
            print("ไม่พบนักศึกษาที่มีรหัสนี้")
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def search(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(f"รหัสนักศึกษา: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next

# สร้าง Linked List
students = LinkedList()

# เพิ่มข้อมูลนักศึกษา
students.append(66030213, "กรรณิการ์ มาอุ่น", 3.0)
students.append(66030281, "วิภัสศศิชา บำเพ็ญบุญ", 3.33)
students.append(66030232, "ณัฐณิชชา กิติชยาโชติ", 3.53)
students.append(66030284, "ศรสวรรค์ จันทสุวรรณโณ", 3.40)

# พิมพ์รายชื่อนักศึกษาทั้งหมด
students.print_list()

# ลบนักศึกษาที่มีรหัส 660302
students.delete(66030232)

# ค้นหานักศึกษาที่มีรหัส 66030284
found_student = students.search(66030284)
if found_student:
    print(f"พบนักศึกษา: {found_student.name}")
else:
    print("ไม่พบนักศึกษา")

# พิมพ์รายชื่อนักศึกษาทั้งหมดอีกครั้ง
students.print_list()
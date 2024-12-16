class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.grade = grade  # เกรด
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป
class LinkedList:
    def __init__(self):
        self.head = None  # หัวของลิสต์ เริ่มต้นเป็น None

    # เพิ่มข้อมูลนักศึกษาลงในลิสต์
    def append(self, student_id, name, grade):
        new_student = Node(student_id, name, grade)
        if not self.head:  # ถ้าลิสต์ว่าง
            self.head = new_student
        else:
            temp = self.head
            while temp.next:  # เดินไปจนถึง Node สุดท้าย
                temp = temp.next
            temp.next = new_student  # เชื่อมโยง Node ใหม่ที่ท้ายลิสต์

    # ลบข้อมูลนักศึกษาตามรหัสนักศึกษา
    def delete(self, student_id):
        temp = self.head
        # ถ้าหัวคือตัวที่ต้องการลบ
        if temp and temp.student_id == student_id:
            self.head = temp.next
            temp = None
            return
        # ค้นหา Node ที่มีรหัสนักศึกษาตรง
        prev = None
        while temp:
            if temp.student_id == student_id:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"ไม่พบข้อมูลของนักศึกษาที่มีรหัส {student_id}")
            return
        prev.next = temp.next  # เชื่อมโยง Node ก่อนหน้ากับ Node ถัดไป
        temp = None  # ลบ Node

    # ค้นหาและแสดงข้อมูลนักศึกษาตามรหัส
    def search(self, student_id):
        temp = self.head
        while temp:
            if temp.student_id == student_id:
                print(f"รหัส: {temp.student_id}, ชื่อ: {temp.name}, เกรด: {temp.grade}")
                return
            temp = temp.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}")

    # แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา
    def display(self):
        if not self.head:
            print("ลิสต์นักศึกษาว่าง")
            return
        # ใช้การเรียงลิสต์ด้วยการเก็บข้อมูลในลิสต์
        students = []
        temp = self.head
        while temp:
            students.append((temp.student_id, temp.name, temp.grade))
            temp = temp.next
        # เรียงตามรหัสนักศึกษา
        students.sort(key=lambda student: student[0])
        print("รายชื่อนักศึกษาทั้งหมด:")
        for student in students:
            print(f"รหัส: {student[0]}, ชื่อ: {student[1]}, เกรด: {student[2]}")
# ตัวอย่างการใช้งาน
linked_list = LinkedList()
# เพิ่มข้อมูลนักศึกษา
linked_list.append(66030196, "นางสาวสิริวรรณ", "A")
linked_list.append(66030158, "นางสาวสวยเลิศปัฐพี", "B+")
linked_list.append(66030178, "นายหล่อวัวตาย", "A")
linked_list.append(66030198, "นายอัครภูมิ"  , "B")
# แสดงข้อมูลทั้งหมด
linked_list.display()
# ค้นหาข้อมูลนักศึกษาตามรหัส
linked_list.search(2)
# ลบข้อมูลนักศึกษาตามรหัส
linked_list.delete(1)
# แสดงข้อมูลทั้งหมดหลังจากลบ
linked_list.display()
# ค้นหาข้อมูลนักศึกษาหลังจากลบ
linked_list.search(1)

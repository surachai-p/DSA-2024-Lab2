class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อ
        self.grade = grade  # เกรด

class Node:
    def __init__(self, student):
        self.student = student  # ข้อมูลของนักศึกษา
        self.next = None  # ชี้ไปที่โหนดถัดไป

class StudentLinkedList:
    def __init__(self):
        self.head = None  # เริ่มต้นด้วย head เป็น None

    # ฟังก์ชันเพิ่มข้อมูลนักศึกษา
    def append(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)
        new_node = Node(new_student)

        if not self.head:  # ถ้า Linked List ว่าง
            self.head = new_node
        else:
            last = self.head
            while last.next:  # เดินไปจนถึงโหนดสุดท้าย
                last = last.next
            last.next = new_node  # เชื่อมโยงโหนดใหม่ที่ท้าย

    # ฟังก์ชันลบข้อมูลนักศึกษาตามรหัสนักศึกษา
    def delete(self, student_id):
        current = self.head
        prev = None
        while current:
            if current.student.student_id == student_id:  # หาเจอรหัสนักศึกษา
                if prev:  # ถ้ามีโหนดก่อนหน้า
                    prev.next = current.next  # ข้ามโหนดนี้ไป
                else:  # ถ้าเป็นโหนดแรก
                    self.head = current.next  # ตั้ง head เป็นโหนดถัดไป
                current = None  # ลบโหนดออก
                return
            prev = current
            current = current.next

    # ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส
    def search(self, student_id):
        current = self.head
        while current:
            if current.student.student_id == student_id:
                return current.student  # ถ้าหาเจอ
            current = current.next
        return None  # ถ้าไม่เจอ

    # ฟังก์ชันแสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา
    def display(self):
        current = self.head
        students = []
        while current:
            students.append(f"รหัส: {current.student.student_id}, ชื่อ: {current.student.name}, เกรด: {current.student.grade}")
            current = current.next
        return students if students else ["ไม่มีข้อมูลนักศึกษา"]

# ฟังก์ชันทดสอบการใช้งาน
def test_student_linked_list():
    sll = StudentLinkedList()

    # เพิ่มข้อมูลนักศึกษา
    sll.append(66030232, "ณัฏฐณิชชา", "B+")
    sll.append(66030238, "ณัฐนันท์", "A")
    sll.append(66030243, "ธัญเทพ", "B")
    sll.append(66030295, "สุวพัชร", "A")

    # แสดงรายชื่อนักศึกษาทั้งหมด
    print("รายชื่อนักศึกษาทั้งหมด:")
    for student in sll.display():
        print(student)

    # ค้นหาข้อมูลนักศึกษาตามรหัส
    student = sll.search(102)
    if student:
        print("\nข้อมูลนักศึกษาที่พบ:")
        print(f"รหัส: {student.student_id}, ชื่อ: {student.name}, เกรด: {student.grade}")
    else:
        print("\nไม่พบข้อมูลนักศึกษาที่รหัสนักศึกษา 66030243")

    # ลบข้อมูลนักศึกษาตามรหัส
    print("\nลบข้อมูลนักศึกษาที่รหัสนักศึกษา 66030243")
    sll.delete(66030243)

    # แสดงรายชื่อนักศึกษาหลังจากลบ
    print("\nรายชื่อนักศึกษาหลังจากลบข้อมูล:")
    for student in sll.display():
        print(student)

# เรียกใช้งาน
test_student_linked_list()

##3.จงเขียนโปรแกรมใช้ Linked List ในการจัดการข้อมูลนักศึกษา โดยมีความสามารถดังนี้:
##1. เพิ่มข้อมูลนักศึกษา (รหัส, ชื่อ, เกรด) 
##2. ลบข้อมูลนักศึกษาตามรหัสนักศึกษา 
##3. ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา
##4. แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา
class StudentNode: ##โหนดที่เก็บข้อมูลนักศึกษา
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None


class StudentLinkedList: ##จัดการข้อมูลนักศึกษา
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, grade):
        new_node = StudentNode(student_id, name, grade) ##เพิ่อมข้อมูลนักศึกษาใหม่
        if not self.head or student_id < self.head.student_id:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.student_id < student_id:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_student(self, student_id): ##ลบข้อมูลนักศึกษา
        if not self.head:
            print("ไม่พบข้อมูลนักศึกษาในระบบ")
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
            return
        current = self.head
        while current.next and current.next.student_id != student_id:
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
        else:
            print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    def find_student(self, student_id): ##ค้นหา
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"พบข้อมูลนักศึกษา: รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    def display_students(self): ##แสดงข้อมูล
        current = self.head
        if not current:
            print("ไม่มีข้อมูลนักศึกษาในระบบ")
            return
        print("รายชื่อนักศึกษา:")
        while current:
            print(f"รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
            current = current.next

def exercise_student_management():
    student_list = StudentLinkedList()

    student_list.add_student(102, "Pim", 3.25) ##ข้อมูลนักศึกษา
    student_list.add_student(101, "Tawan", 3.69)
    student_list.add_student(103, "Por", 3.87)

    print("\n1. แสดงรายชื่อนักศึกษาทั้งหมด:")
    student_list.display_students()
    print("\n2. ค้นหานักศึกษารหัส 102:")
    student_list.find_student(102)
    print("\n3. ลบนักศึกษารหัส 101:")
    student_list.delete_student(101)
    print("\n4. แสดงรายชื่อนักศึกษาทั้งหมดหลังลบ:")
    student_list.display_students()
exercise_student_management()
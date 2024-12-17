# คลาส Node สำหรับเก็บข้อมูลนักศึกษา
class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name              # ชื่อนักศึกษา
        self.grade = grade            # เกรดนักศึกษา
        self.next = None              # ตัวชี้ไปยัง Node ถัดไป
# คลาส LinkedList สำหรับการจัดการข้อมูลนักศึกษา
class StudentLinkedList:
    def __init__(self):
        self.head = None
# 1. เพิ่มข้อมูลนักศึกษา
    def add_student(self, student_id, name, grade):
        new_node = Node(student_id, name, grade)
        if not self.head or student_id < self.head.student_id:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.student_id < student_id:
            current = current.next
        new_node.next = current.next
        current.next = new_node
# 2. ลบข้อมูลนักศึกษาตามรหัส
    def delete_student(self, student_id):
        current = self.head
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if not current:
            print(f"ไม่พบรหัสนักศึกษา {student_id}")
            return
        if not prev:  # ลบ Node แรก
            self.head = current.next
        else:  # ลบ Node ตรงกลางหรือท้าย
            prev.next = current.next
        print(f"ลบรหัสนักศึกษา {student_id} สำเร็จ")
# 3. ค้นหาและแสดงข้อมูลนักศึกษาตามรหัส
    def search_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"พบข้อมูล: รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลรหัสนักศึกษา {student_id}")
# 4. แสดงรายชื่อนักศึกษาทั้งหมด
    def display_students(self):
        current = self.head
        if not current:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        print("รายชื่อนักศึกษา:")
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next
# ทดสอบการใช้งาน
if __name__ == "__main__":
    students = StudentLinkedList()    
# เพิ่มข้อมูลนักศึกษา
    students.add_student(66030194, "สุภาวดี", "3.85")
    students.add_student(66030094, "เนตรชนก", "4.00")
    students.add_student(66030067, "ธนกฤษ", "3.67")
    students.add_student(66030083, "นวพล", "4.00")   
# แสดงรายชื่อนักศึกษาทั้งหมด
    print("\nแสดงรายชื่อนักศึกษาทั้งหมด:")
    students.display_students()
# ค้นหาข้อมูลนักศึกษา
    print("\nค้นหาข้อมูลนักศึกษารหัส 66030094:")
    students.search_student(66030094)
# ลบข้อมูลนักศึกษา
    print("\nลบข้อมูลนักศึกษารหัส 66030194:")
    students.delete_student(66030194)
# แสดงรายชื่อนักศึกษาหลังลบ
    print("\nแสดงรายชื่อนักศึกษาหลังลบ:")
    students.display_students()


# โครงสร้าง Node
class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None

# โครงสร้าง Linked List
class StudentLinkedList:
    def __init__(self):
        self.head = None

    # เพิ่มข้อมูลนักศึกษา
    def add_student(self, student_id, name, grade):
        new_node = Node(student_id, name, grade)
        if not self.head or self.head.student_id > student_id:
            # เพิ่มที่หัว ถ้ารหัสที่เพิ่มต้องอยู่ก่อนหน้า
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.student_id < student_id:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # ลบข้อมูลนักศึกษาตามรหัส
    def remove_student(self, student_id):
        current = self.head
        if not current:
            print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")
            return

        # ลบหัวรายการ
        if current.student_id == student_id:
            self.head = current.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
            return

        # ค้นหา Node ที่ต้องการลบ
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
        else:
            print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    # ค้นหาและแสดงข้อมูลนักศึกษาตามรหัส
    def search_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    # แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัส
    def display_students(self):
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        current = self.head
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next

# ทดสอบการใช้งาน
students = StudentLinkedList()

# เพิ่มข้อมูลนักศึกษา
students.add_student(66030270, "Phum", 3.8)
students.add_student(66030001, "sudlor", 2.2)
students.add_student(66030002, "sudsuy", 3.1)

# แสดงรายชื่อนักศึกษาทั้งหมด
print("รายชื่อนักศึกษาทั้งหมด:")
students.display_students()

# ค้นหานักศึกษา
print("\nค้นหานักศึกษารหัส 66030270:")
students.search_student(66030270)

# ลบข้อมูลนักศึกษา
print("\nลบนักศึกษารหัส 66030001:")
students.remove_student(66030001)

# แสดงรายชื่อนักศึกษาหลังจากลบ
print("\nรายชื่อนักศึกษาหลังจากลบ:")
students.display_students()

class Node:
    """โครงสร้างของ Node สำหรับข้อมูลนักศึกษาใน Linked List"""
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.grade = grade  # เกรดนักศึกษา
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป

class StudentLinkedList:
    """โครงสร้างของ Linked List สำหรับจัดการข้อมูลนักศึกษา"""
    def __init__(self):
        self.head = None  # หัวของ Linked List

    def add_student(self, student_id, name, grade):
        """เพิ่มข้อมูลนักศึกษาใหม่ใน Linked List โดยเรียงตามรหัสนักศึกษา"""
        new_node = Node(student_id, name, grade)
        if not self.head or student_id < self.head.student_id:  # เพิ่มที่หัวถ้ารหัสเล็กสุด
            new_node.next = self.head
            self.head = new_node
        else:  # หา Node ที่ตำแหน่งเหมาะสม
            current = self.head
            while current.next and current.next.student_id < student_id:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_student(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษาในระบบ")
            return
        if self.head.student_id == student_id:  # ลบหัว Node
            self.head = self.head.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
            return
        current = self.head
        while current.next:
            if current.next.student_id == student_id:
                current.next = current.next.next
                print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    def search_student(self, student_id):
        """ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head
        while current:
            if current.student_id == student_id:
                print("\nพบข้อมูลนักศึกษา:")
                print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    def display_students(self):
        """แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา"""
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษาในระบบ")
            return
        current = self.head
        print("\nรายชื่อนักศึกษา:")
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next

# ฟังก์ชันทดสอบการทำงานของโปรแกรม
def manage_students():
    student_list = StudentLinkedList()
    while True:
        print("\n===== ระบบจัดการข้อมูลนักศึกษา =====")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษาตามรหัส")
        print("3. ค้นหาและแสดงข้อมูลนักศึกษาตามรหัส")
        print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
        print("5. ออกจากโปรแกรม")

        choice = input("เลือกคำสั่ง (1-5): ")
        if choice == '1':
            student_id = input("ป้อนรหัสนักศึกษา: ")
            name = input("ป้อนชื่อนักศึกษา: ")
            grade = input("ป้อนเกรดนักศึกษา: ")
            student_list.add_student(student_id, name, grade)
        elif choice == '2':
            student_id = input("ป้อนรหัสนักศึกษาที่ต้องการลบ: ")
            student_list.delete_student(student_id)
        elif choice == '3':
            student_id = input("ป้อนรหัสนักศึกษาที่ต้องการค้นหา: ")
            student_list.search_student(student_id)
        elif choice == '4':
            student_list.display_students()
        elif choice == '5':
            print("\nออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กรุณาเลือกคำสั่งให้ถูกต้อง")

# เรียกใช้งานโปรแกรม
manage_students()

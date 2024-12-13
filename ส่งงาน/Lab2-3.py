class Node:
    """Class to represent a node in a linked list."""
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None

class StudentLinkedList:
    """Class to represent a linked list for managing student data."""
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, grade):
        """Add a new student to the linked list in sorted order by student ID."""
        new_node = Node(student_id, name, grade)
        if not self.head or self.head.student_id > student_id:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.student_id < student_id:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove_student(self, student_id):
        """Remove a student from the list by their student ID."""
        current = self.head
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next

        if not current:
            print(f"ไม่พบรหัสนักศึกษา {student_id}")
            return

        if not prev:  # The student to remove is the head
            self.head = current.next
        else:
            prev.next = current.next
        print(f"ลบนักศึกษารหัส {student_id} สำเร็จ")

    def search_student(self, student_id):
        """Search for a student by their student ID."""
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"พบข้อมูลนักศึกษา: รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
                return
            current = current.next
        print(f"ไม่พบรหัสนักศึกษา {student_id}")

    def display_students(self):
        """Display all students in the list sorted by student ID."""
        current = self.head
        if not current:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        print("รายชื่อนักศึกษาทั้งหมด:")
        while current:
            print(f"รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
            current = current.next

# โปรแกรมหลัก
student_list = StudentLinkedList()

while True:
    print("\nจัดการข้อมูลนักศึกษา:")
    print("1. เพิ่มข้อมูลนักศึกษา")
    print("2. ลบข้อมูลนักศึกษาตามรหัส")
    print("3. ค้นหาข้อมูลนักศึกษาตามรหัส")
    print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
    print("5. ออกจากโปรแกรม")
    choice = input("เลือกคำสั่ง: ")

    if choice == "1":
        student_id = int(input("กรอกรหัสนักศึกษา: "))
        name = input("กรอกชื่อนักศึกษา: ")
        grade = float(input("กรอกเกรด: "))
        student_list.add_student(student_id, name, grade)
        print("เพิ่มข้อมูลสำเร็จ!")
    elif choice == "2":
        student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการลบ: "))
        student_list.remove_student(student_id)
    elif choice == "3":
        student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
        student_list.search_student(student_id)
    elif choice == "4":
        student_list.display_students()
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("เลือกคำสั่งไม่ถูกต้อง! กรุณาลองใหม่")

class Student:
    """โครงสร้างของ Node สำหรับข้อมูลนักศึกษา"""
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None

class StudentLinkedList:
    """โครงสร้างของ Linked List สำหรับจัดการข้อมูลนักศึกษา"""
    def __init__(self):
        self.head = None

    def append(self, student_id, name, grade):
        """เพิ่มข้อมูลนักศึกษาใหม่ที่ท้าย Linked List"""
        new_student = Student(student_id, name, grade)
        if not self.head:
            self.head = new_student
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_student

    def delete(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if current is None:  # รหัสนักศึกษานี้ไม่พบ
            print("ไม่พบข้อมูลนักศึกษาที่รหัส", student_id)
            return
        if prev is None:  # ถ้าเป็นหัวของ Linked List
            self.head = current.next
        else:
            prev.next = current.next
        print(f"ลบข้อมูลนักศึกษารหัส {student_id} เรียบร้อย")

    def search(self, student_id):
        """ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัสนักศึกษา: {current.student_id}, ชื่อนักศึกษา: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print("ไม่พบข้อมูลนักศึกษาที่รหัส", student_id)

    def display_all(self):
        """แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา"""
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        students = []
        current = self.head
        while current:
            students.append((current.student_id, current.name, current.grade))
            current = current.next
        students.sort()  # เรียงตามรหัสนักศึกษา
        print("รายชื่อนักศึกษาทั้งหมด:")
        for student in students:
            print(f"รหัสนักศึกษา: {student[0]}, ชื่อนักศึกษา: {student[1]}, เกรด: {student[2]}")

# ฟังก์ชันสำหรับกรอกข้อมูลนักศึกษา
def input_student_data():
    student_id = int(input("กรอกรหัสนักศึกษา: "))
    name = input("กรอกชื่อ: ")
    grade = input("กรอกเกรด: ")
    return student_id, name, grade

def menu():
    print("\nเมนู:")
    print("1. เพิ่มข้อมูลนักศึกษา")
    print("2. ลบข้อมูลนักศึกษาตามรหัสนักศึกษา")
    print("3. ค้นหานักศึกษาตามรหัสนักศึกษา")
    print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
    print("5. ออกจากโปรแกรม")

def main():
    student_list = StudentLinkedList()

    while True:
        menu()
        choice = input("กรุณาเลือกเมนู (1-5): ")

        if choice == '1':
            student_id, name, grade = input_student_data()
            student_list.append(student_id, name, grade)
        elif choice == '2':
            student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการลบ: "))
            student_list.delete(student_id)
        elif choice == '3':
            student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student_list.search(student_id)
        elif choice == '4':
            student_list.display_all()
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()

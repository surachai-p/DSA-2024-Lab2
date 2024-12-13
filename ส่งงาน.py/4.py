class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.grade = grade  # เกรด
        self.next = None  # ตัวเชื่อมไปยังนักศึกษาถัดไปใน Linked List

class StudentList:
    def __init__(self):
        self.head = None  # หัวของ Linked List

    # เพิ่มข้อมูลนักศึกษาใหม่
    def add_student(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    # ลบข้อมูลนักศึกษาตามรหัสนักศึกษา
    def delete_student(self, student_id):
        current = self.head
        previous = None
        while current:
            if current.student_id == student_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"ลบข้อมูลนักศึกษาที่มีรหัส {student_id} เรียบร้อยแล้ว")
                return
            previous = current
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}")

    # ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา
    def find_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"ข้อมูลนักศึกษาที่พบ: รหัส = {current.student_id}, ชื่อ = {current.name}, เกรด = {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}")

    # แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา
    def display_all_students(self):
        students = []
        current = self.head
        while current:
            students.append((current.student_id, current.name, current.grade))
            current = current.next
        
        # เรียงตามรหัสนักศึกษา
        students.sort(key=lambda x: x[0])

        if students:  # ถ้ามีข้อมูลใน Linked List
            for student in students:
                print(f"รหัส = {student[0]}, ชื่อ = {student[1]}, เกรด = {student[2]}")
        else:
            print("ไม่มีข้อมูลนักศึกษาในระบบ")

# ฟังก์ชันหลักในการให้ผู้ใช้กรอกข้อมูล
def main():
    student_list = StudentList()

    while True:
        print("\nเมนู:")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษา")
        print("3. ค้นหาข้อมูลนักศึกษา")
        print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-5): ")

        if choice == "1":
            student_id = int(input("กรุณากรอกรหัสนักศึกษา: "))
            name = input("กรุณากรอกชื่อของนักศึกษา: ")
            grade = input("กรุณากรอกเกรดของนักศึกษา: ")
            student_list.add_student(student_id, name, grade)
            print("เพิ่มข้อมูลนักศึกษาสำเร็จ")
        
        elif choice == "2":
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการลบ: "))
            student_list.delete_student(student_id)
        
        elif choice == "3":
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student_list.find_student(student_id)
        
        elif choice == "4":
            print("\nรายชื่อนักศึกษาทั้งหมด:")
            student_list.display_all_students()
        
        elif choice == "5":
            print("ขอบคุณที่ใช้โปรแกรม")
            break
        
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()


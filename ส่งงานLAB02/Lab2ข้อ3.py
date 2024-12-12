class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.grade = grade  # เกรด
        self.next = None  # ตัวชี้ไปยังโหนดถัดไป

class StudentLinkedList:
    def __init__(self):
        self.head = None  # เริ่มต้นด้วยลิสต์ว่าง

    # เพิ่มข้อมูลนักศึกษา
    def append(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)  # สร้างโหนดใหม่
        if not self.head:  # ถ้าลิสต์ว่าง
            self.head = new_student  # กำหนดโหนดใหม่เป็นหัว
            return
        last_student = self.head
        while last_student.next:  # ค้นหาท้ายของลิสต์
            last_student = last_student.next
        last_student.next = new_student  # เชื่อมโหนดใหม่ที่ท้าย

    # ลบข้อมูลนักศึกษาตามรหัส
    def delete(self, student_id):
        current = self.head
        if current and current.student_id == student_id:  # ถ้าเป็นโหนดแรก
            self.head = current.next  # กำหนดหัวใหม่
            current = None
            return
        prev = None
        while current:
            if current.student_id == student_id:
                if prev:
                    prev.next = current.next  # ลบโหนด
                current = None
                return
            prev = current
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}")

    # ค้นหานักศึกษาตามรหัส
    def search(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัสนักศึกษา: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}")

    # แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัส
    def display(self):
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        students = []
        current = self.head
        while current:
            students.append((current.student_id, current.name, current.grade))
            current = current.next
        # เรียงลำดับตามรหัสนักศึกษา
        students.sort(key=lambda x: x[0])
        print("รายชื่อนักศึกษาทั้งหมด (เรียงตามรหัส):")
        for student in students:
            print(f"รหัสนักศึกษา: {student[0]}, ชื่อ: {student[1]}, เกรด: {student[2]}")

# ฟังก์ชันเพื่อรับข้อมูลจากผู้ใช้
def main():
    student_list = StudentLinkedList()

    while True:
        print("\nเลือกการทำงาน:")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษา")
        print("3. ค้นหาข้อมูลนักศึกษา")
        print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-5): ")

        if choice == '1':
            student_id = int(input("กรุณากรอกรหัสนักศึกษา: "))
            name = input("กรุณากรอกชื่อนักศึกษา: ")
            grade = input("กรุณากรอกเกรดนักศึกษา: ")
            student_list.append(student_id, name, grade)
            print("เพิ่มข้อมูลนักศึกษาสำเร็จ!")

        elif choice == '2':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการลบ: "))
            student_list.delete(student_id)

        elif choice == '3':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student_list.search(student_id)

        elif choice == '4':
            student_list.display()

        elif choice == '5':
            print("ขอบคุณที่ใช้โปรแกรม!")
            break

        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่.")

# เรียกใช้ฟังก์ชันหลัก
main()

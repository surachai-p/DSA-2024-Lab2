# สร้างคลาส Node เพื่อแทนข้อมูลนักศึกษา
class StudentNode:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.grade = grade  # เกรดของนักศึกษา
        self.next = None  # ตัวชี้ไปยังโหนดถัดไป

# สร้างคลาส LinkedList เพื่อจัดการข้อมูลนักศึกษา
class StudentLinkedList:
    def __init__(self):
        self.head = None  # ตัวชี้ไปยังหัวของลิสต์

    # ฟังก์ชันเพิ่มนักศึกษาในลิสต์
    def add_student(self, student_id, name, grade):
        new_student = StudentNode(student_id, name, grade)
        if not self.head:
            self.head = new_student
        else:
            last = self.head
            while last.next:  # หาตำแหน่งสุดท้ายของลิสต์
                last = last.next
            last.next = new_student

    # ฟังก์ชันแสดงข้อมูลทั้งหมดของนักศึกษา
    def display_students(self):
        current = self.head
        if not current:
            print("ไม่มีข้อมูลนักศึกษาในลิสต์.")
            return
        while current:
            print(f"รหัสนักศึกษา: {current.student_id}, ชื่อนักศึกษา: {current.name}, เกรด: {current.grade}")
            current = current.next

    # ฟังก์ชันค้นหานักศึกษาจากรหัสนักศึกษา
    def search_student_by_id(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"พบข้อมูลนักศึกษา: รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}.")

    # ฟังก์ชันลบข้อมูลนักศึกษาจากรหัสนักศึกษา
    def delete_student_by_id(self, student_id):
        current = self.head
        prev = None
        while current:
            if current.student_id == student_id:
                if prev is None:  # ถ้าคือโหนดแรก
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ.")
                return
            prev = current
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษาที่มีรหัส {student_id}.")

# สร้าง StudentLinkedList และทดสอบการใช้งาน
student_list = StudentLinkedList()

# เพิ่มข้อมูลนักศึกษาพร้อมเกรด
student_list.add_student(66030010, "กันตพัฒน์", "4.00")
student_list.add_student(66030029, "จิรสิน", "4.00")
student_list.add_student(66030238, "ธัญเทพ", "3.98")

# แสดงข้อมูลนักศึกษาทั้งหมด
print("ข้อมูลนักศึกษาทั้งหมด:")
student_list.display_students()

# ค้นหานักศึกษาจากรหัส
print("\nค้นหานักศึกษารหัส 66030010:")
student_list.search_student_by_id(66030010)

# ลบข้อมูลนักศึกษาจากรหัส
print("\nลบข้อมูลนักศึกษารหัส 66030029:")
student_list.delete_student_by_id(66030029)

# แสดงข้อมูลนักศึกษาหลังจากลบ
print("\nข้อมูลนักศึกษาหลังจากลบรหัส 66030029:")
student_list.display_students()

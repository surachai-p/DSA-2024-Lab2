class StudentNode:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name              # ชื่อนักศึกษา
        self.grade = grade            # เกรดนักศึกษา
        self.next = None              # ตัวชี้ไปยัง Node ถัดไป

class StudentLinkedList:
    def __init__(self):
        self.head = None              # หัวของ Linked List

    def add_student(self, student_id, name, grade):
        """เพิ่มข้อมูลนักศึกษาเรียงตามรหัสนักศึกษา"""
        new_node = StudentNode(student_id, name, grade)
        
        # กรณี List ว่างหรือรหัสนักศึกษาใหม่ น้อยกว่าหัว
        if not self.head or student_id < self.head.student_id:
            new_node.next = self.head
            self.head = new_node
            return
        
        # หา Node ตำแหน่งที่เหมาะสมในการแทรก
        current = self.head
        while current.next and current.next.student_id < student_id:
            current = current.next
        
        # เพิ่ม Node ใหม่ที่ตำแหน่งที่เหมาะสม
        new_node.next = current.next
        current.next = new_node

    def delete_student(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head

        # กรณีลบ Node แรก
        if current and current.student_id == student_id:
            self.head = current.next
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} สำเร็จ")
            return
        
        # ค้นหา Node ที่จะลบ
        while current and current.next:
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
                print(f"พบข้อมูลนักศึกษา: รหัส {current.student_id}, ชื่อ {current.name}, เกรด {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

    def display_students(self):
        """แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา"""
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        
        print("ข้อมูลนักศึกษาทั้งหมด:")
        current = self.head
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next

# ฟังก์ชันหลักสำหรับเมนู
def main():
    student_list = StudentLinkedList()

    while True:
        print("\n--- ระบบจัดการข้อมูลนักศึกษา ---")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษา")
        print("3. ค้นหาข้อมูลนักศึกษา")
        print("4. แสดงรายชื่อนักศึกษาทั้งหมด")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-5): ")

        if choice == "1":
            try:
                student_id = int(input("ป้อนรหัสนักศึกษา (3 หลักท้าย): "))
                name = input("ป้อนชื่อนักศึกษา (ภาษาไทย) : ")
                grade = input("ป้อนเกรดนักศึกษา: ")
                student_list.add_student(student_id, name, grade)
                print("เพิ่มข้อมูลนักศึกษาเรียบร้อย")
            except ValueError:
                print("รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น!")

        elif choice == "2":
            try:
                student_id = int(input("ป้อนรหัสนักศึกษาที่ต้องการลบ: "))
                student_list.delete_student(student_id)
            except ValueError:
                print("รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น!")

        elif choice == "3":
            try:
                student_id = int(input("ป้อนรหัสนักศึกษาที่ต้องการค้นหา: "))
                student_list.search_student(student_id)
            except ValueError:
                print("รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น!")

        elif choice == "4":
            student_list.display_students()

        elif choice == "5":
            print("ออกจากโปรแกรม...")
            break

        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง (1-5)")

if __name__ == "__main__":
    main()

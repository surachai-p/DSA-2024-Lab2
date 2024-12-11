class StudentNode:
    """โครงสร้างของ Node สำหรับจัดเก็บข้อมูลนักศึกษาใน Doubly Linked List"""
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None
        self.prev = None

class StudentLinkedList:
    """โครงสร้างของ Doubly Linked List สำหรับข้อมูลนักศึกษา"""
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, grade):
        """เพิ่มข้อมูลนักศึกษาเรียงตามรหัสนักศึกษา"""
        new_node = StudentNode(student_id, name, grade)
        if not self.head or self.head.student_id > student_id:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.student_id < student_id:
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def delete_student(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head

        while current:
            if current.student_id == student_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f"ลบข้อมูลนักศึกษา รหัส {student_id} เรียบร้อยแล้ว")
                return
            current = current.next

        print(f"ไม่พบข้อมูลนักศึกษา รหัส {student_id}")

    def search_student(self, student_id):
        """ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา"""
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลนักศึกษา รหัส {student_id}")

    def display_students(self):
        """แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา"""
        current = self.head
        if not current:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        print("รายชื่อนักศึกษา:")
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next

# ฟังก์ชันหลักสำหรับจัดการข้อมูลนักศึกษา
def main():
    student_list = StudentLinkedList()

    while True:
        print("\nโปรดเลือกคำสั่ง:")
        print("1: เพิ่มข้อมูลนักศึกษา")
        print("2: ลบข้อมูลนักศึกษาตามรหัส")
        print("3: ค้นหาข้อมูลนักศึกษาตามรหัส")
        print("4: แสดงรายชื่อนักศึกษาทั้งหมด")
        print("5: ออกจากโปรแกรม")

        choice = input("กรุณาเลือกคำสั่ง (1-5): ")

        if choice == '1':
            student_id = int(input("ป้อนรหัสนักศึกษา: "))
            name = input("ป้อนชื่อนักศึกษา: ")
            grade = input("ป้อนเกรดนักศึกษา: ")
            student_list.add_student(student_id, name, grade)
            print(f"เพิ่มข้อมูลนักศึกษา รหัส {student_id} เรียบร้อยแล้ว")

        elif choice == '2':
            student_id = int(input("ป้อนรหัสนักศึกษาที่ต้องการลบ: "))
            student_list.delete_student(student_id)

        elif choice == '3':
            student_id = int(input("ป้อนรหัสนักศึกษาที่ต้องการค้นหา: "))
            student_list.search_student(student_id)

        elif choice == '4':
            student_list.display_students()

        elif choice == '5':
            print("ออกจากโปรแกรม")
            break

        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้งานโปรแกรมหลัก
if __name__ == "__main__":
    main()

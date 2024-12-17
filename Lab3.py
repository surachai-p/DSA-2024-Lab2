class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def append(self, student_id, name, grade):
        new_node = Node(student_id, name, grade)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_student(self, student_id):
        current = self.head
        previous = None
        while current:
            if current.student_id == student_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"ต้องการจะลบข้อมูล กรอกรหัสนักศึกษา: {student_id}")
                return
            previous = current
            current = current.next
        print(f"ไม่พบข้อมูลของนักศึกษา {student_id} ")

    def find_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัสนักศึกษา : {current.student_id}, ชื่อ - สกุล : {current.name}, เกรด : {current.grade}")
                return
            current = current.next
        print(f"ไม่พบข้อมูลของนักศึกษา {student_id} ")

    def display_all_students(self):
        if not self.head:
            print("ไม่พบข้อมูลของนักศึกษ")
            return
        current = self.head
        students = []
        while current:
            students.append((current.student_id, current.name, current.grade))
            current = current.next
        
        students.sort(key=lambda x: x[0])
        print("รายชื่อนักเรียน :")
        for student in students:
            print(f"รหัสนักศึกษา : {student[0]}, ชื่อ - สกุล : {student[1]}, เกรด : {student[2]}")

def input_student_data():
    try:
        student_id = int(input("กรอกรหัส นักศึกษา : "))
        name = input("กรอกชื่อ - นามสกุล: ")
        grade = input("กรอกเกรดที่ได้ : ")
        return student_id, name, grade
    except ValueError:
        print("ข้อมูลไม่ถูกต้อง รหัสนักศึกษาต้องเป็นจำนวนเต็ม")
        return None



student_list = StudentList()

while True:
        print("\nป้อนข้อมูลนักศึกษา")
        student_data = input_student_data()
        if student_data:
            student_id, name, grade = student_data
            student_list.append(student_id, name, grade)
    
        more = input("คุณต้องการเพิ่มนักเรียนคนอื่นหรือไม่? (y/n) : ")
        if more.lower() != 'y':
            break

student_list.display_all_students()

search_id = int(input("\nกรอกรหัสนักศึกษาเพื่อค้นหา :"))
student_list.find_student(search_id)

delete_id = int(input("\nกรอกรหัสนักศึกษาที่ต้องการลบ : "))
student_list.remove_student(delete_id)

student_list.display_all_students()

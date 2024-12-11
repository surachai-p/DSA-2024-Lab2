class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id  
        self.name = name  
        self.grade = grade  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

   
    def append(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)
        if not self.head:  
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    
    def delete(self, student_id):
        current = self.head
        if current and current.student_id == student_id:  
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if current:  # ถ้าพบ
            prev.next = current.next
            current = None

    
    def search(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None

    
    def display_all(self):
        current = self.head
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Grade: {current.grade}")
            current = current.next

    
    def display_sorted(self):
        students = []
        current = self.head
        while current:
            students.append((current.student_id, current.name, current.grade))
            current = current.next
        students.sort()  
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")


student_list = LinkedList()
student_list.append(66030243, "ธัญเทพ หาญกล้า", "4.00")
student_list.append(66030010, "กันตพัฒน์ ตั้งกิตติธารา", "3.98")
student_list.append(66030232, "ณัฏฐณิชชา กิติชยาโชติ", "2.50")


print("ข้อมูลนักศึกษาทั้งหมด:")
student_list.display_all()


print("\nค้นหานักศึกษาที่มีรหัส 66030243:")
student = student_list.search(66030243)
if student:
    print(f"พบข้อมูล: ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
else:
    print("ไม่พบข้อมูลนักศึกษานี้")


print("\nลบข้อมูลนักศึกษาที่มีรหัส 66030010:")
student_list.delete(66030010)


print("\nข้อมูลนักศึกษาหลังจากลบ:")
student_list.display_sorted()

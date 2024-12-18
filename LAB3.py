class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)
        if self.head is None or self.head.student_id > student_id:
            new_student.next = self.head
            self.head = new_student
        else:
            current = self.head
            while current.next and current.next.student_id < student_id:
                current = current.next
            new_student.next = current.next
            current.next = new_student
        print(f"Added student: ID={student_id}, Name={name}, Grade={grade}")

    def remove_student(self, student_id):
        if self.head is None:
            print("Student list is empty.")
            return

        if self.head.student_id == student_id:
            self.head = self.head.next
            print(f"Removed student with ID {student_id}")
            return

        current = self.head
        while current.next and current.next.student_id != student_id:
            current = current.next

        if current.next is None:
            print(f"Student with ID {student_id} not found.")
        else:
            current.next = current.next.next
            print(f"Removed student with ID {student_id}")

    def find_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"Found student: ID={current.student_id}, Name={current.name}, Grade={current.grade}")
                return
            current = current.next
        print(f"Student with ID {student_id} not found.")

    def display_students(self):
        if self.head is None:
            print("No students in the list.")
            return

        print("Student List:")
        current = self.head
        while current:
            print(f"ID={current.student_id}, Name={current.name}, Grade={current.grade}")
            current = current.next

student_list = StudentLinkedList()
student_list.add_student(101, "Alice", "A")
student_list.add_student(103, "Bob", "B")
student_list.add_student(102, "Charlie", "C")

student_list.display_students()

student_list.find_student(102)

student_list.remove_student(101)

student_list.display_students()

# การทดลองที่ X: การใช้งานโครงสร้างข้อมูลแบบ Linked List

## วัตถุประสงค์
1. เพื่อให้สามารถอธิบายหลักการทำงานของโครงสร้างข้อมูลแบบ Linked List
2. เพื่อให้สามารถเขียนโปรแกรมจัดการ Linked List ด้วยภาษา Python ได้
3. เพื่อให้สามารถประยุกต์ใช้ Linked List ในการแก้ปัญหาได้

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. Python IDE (เช่น PyCharm, VS Code)
3. ใบงานการทดลอง

## ทฤษฎีที่เกี่ยวข้อง
Linked List เป็นโครงสร้างข้อมูลที่เก็บข้อมูลในรูปแบบต่อเนื่องกันเป็นเหมือนลูกโซ่ โดยแต่ละ Node จะประกอบด้วย:
- ส่วนเก็บข้อมูล (Data)
- ส่วนเก็บที่อยู่ของ Node ถัดไป (Next Pointer)

### ประเภทของ Linked List
1. Singly Linked List: แต่ละ Node มี pointer ชี้ไปข้างหน้าอย่างเดียว
2. Doubly Linked List: แต่ละ Node มี pointer ชี้ไปทั้งข้างหน้าและข้างหลัง
3. Circular Linked List: Node สุดท้ายจะชี้กลับมาที่ Node แรก

## การทดลอง

### ส่วนที่ 1: การสร้างโครงสร้างพื้นฐาน

```python
class Node:
    def __init__(self, data):
        self.data = data    # เก็บข้อมูลของ Node
        self.next = None    # pointer ชี้ไป Node ถัดไป

class LinkedList:
    def __init__(self):
        self.head = None    # กำหนด head เริ่มต้นเป็น None (List ว่าง)
```

**คำอธิบาย:**
- คลาส Node เป็นโครงสร้างพื้นฐานที่ใช้เก็บข้อมูลแต่ละตัวใน Linked List
- คลาส LinkedList ใช้สำหรับจัดการ Node ทั้งหมด โดยมี head เป็นตัวชี้ไปยัง Node แรก

### ส่วนที่ 2: การเพิ่มข้อมูล

```python
def append(self, data):
    """เพิ่มข้อมูลที่ท้าย Linked List"""
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node

def prepend(self, data):
    """เพิ่มข้อมูลที่หน้า Linked List"""
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

**คำอธิบาย:**
- `append()`: เพิ่มข้อมูลที่ท้าย List
  1. สร้าง Node ใหม่
  2. ถ้า List ว่าง ให้ head ชี้ไปที่ Node ใหม่
  3. ถ้าไม่ว่าง วิ่งไปท้าย List แล้วเพิ่ม Node ใหม่
- `prepend()`: เพิ่มข้อมูลที่หน้า List
  1. สร้าง Node ใหม่
  2. ให้ Node ใหม่ชี้ไปที่ head เดิม
  3. เปลี่ยน head ให้ชี้มาที่ Node ใหม่

### ส่วนที่ 3: การลบข้อมูล

```python
def delete(self, key):
    """ลบข้อมูลที่ต้องการออกจาก List"""
    current = self.head
    
    # กรณีลบ Node แรก
    if current and current.data == key:
        self.head = current.next
        return
        
    # กรณีลบ Node อื่นๆ
    while current and current.next:
        if current.next.data == key:
            current.next = current.next.next
            return
        current = current.next
```

**คำอธิบาย:**
- ฟังก์ชันรับค่า key ที่ต้องการลบ
- ตรวจสอบกรณีลบ Node แรก (head)
- วนลูปหาข้อมูลที่ต้องการลบ แล้วเปลี่ยน pointer ข้าม Node นั้น

### ส่วนที่ 4: การแสดงและค้นหาข้อมูล

```python
def display(self):
    """แสดงข้อมูลทั้งหมดใน List"""
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def search(self, key):
    """ค้นหาข้อมูลใน List"""
    current = self.head
    position = 0
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    return -1
```

**คำอธิบาย:**
- `display()`: แสดงข้อมูลทั้งหมดเรียงจากหน้าไปหลัง
- `search()`: ค้นหาข้อมูลและคืนค่าตำแหน่งที่พบ (-1 ถ้าไม่พบ)

## แบบฝึกหัดระหว่างการทดลอง

### แบบฝึกหัดที่ 1: การสร้างและจัดการ Linked List พื้นฐาน
```python
def exercise1():
    # สร้าง Linked List ใหม่
    llist = LinkedList()
    
    # เพิ่มข้อมูล
    print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("ผลลัพธ์:")
    llist.display()
    
    # เพิ่มข้อมูลที่หน้า List
    print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
    llist.prepend(0)
    print("ผลลัพธ์:")
    llist.display()
    
    # ลบข้อมูล
    print("\n3. ลบข้อมูล 2")
    llist.delete(2)
    print("ผลลัพธ์:")
    llist.display()
```

### แบบฝึกหัดที่ 2: การนับและค้นหาข้อมูล
```python
def count_nodes(llist):
    """นับจำนวน Node ทั้งหมด"""
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

# ทดสอบการใช้งาน
llist = LinkedList()
for i in range(5):
    llist.append(i)

print("Linked List ที่สร้าง:")
llist.display()
print(f"จำนวน Node ทั้งหมด: {count_nodes(llist)}")
```

## แบบทดสอบท้ายการทดลอง
### 1.จงเขียนโปรแกรมเพื่อสร้าง Doubly Linked-List


### 2.จงเขียนโปรแกรมใช้ Linked List ในการจัดการข้อมูลนักศึกษา โดยมีความสามารถดังนี้:
1. เพิ่มข้อมูลนักศึกษา (รหัส, ชื่อ, เกรด) 
2. ลบข้อมูลนักศึกษาตามรหัสนักศึกษา 
3. ค้นหาและแสดงข้อมูลนักศึกษาตามรหัสนักศึกษา
4. แสดงรายชื่อนักศึกษาทั้งหมดเรียงตามรหัสนักศึกษา


## การส่งงาน
1. ส่งไฟล์ .py ที่มีโค้ดทั้งหมด


## หมายเหตุ
- อนุญาตให้ใช้เอกสารประกอบการเรียนในระหว่างการทดลอง
- ไม่อนุญาตให้คัดลอกงานผู้อื่น
- คะแนนจะถูกหักหากส่งงานช้ากว่ากำหนด

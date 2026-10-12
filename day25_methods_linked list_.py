Python

class Details:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def change_age(self, new_age):
        self.age = new_age


details1 = Details("anku", 19, 739)
details1.display()

details1.change_age(20)
print("Updated age:", details1.age)


class Student:
    def __init__(self, name, age, hallticket, group, marks):
        self.name = name
        self.age = age
        self.hallticket = hallticket
        self.group = group
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Hall ticket:", self.hallticket)
        print("Group:", self.group)
        print("Marks:", self.marks)

    def change_marks(self, new_marks):

        self.marks = new_marks


student1 = Student(
    "maseera", 18, 839490268, "BSc Data Science", 738
)
student1.display()

student1.change_marks(962)
print("Updated marks:", student1.marks)

dsa
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create six nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

# Connect the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# 1. Traverse and print all nodes
print("Linked list:")
current = node1

while current is not None:
    print(current.data)
    current = current.next

# 2. Search for a value
target = 30
current = node1
found = False

while current is not None:
    if current.data == target:
        found = True
        break
    current = current.next

if found:
    print("Found:", target)
else:
    print("Not found:", target)

# 3. Count all nodes
current = node1
count = 0

while current is not None:
    count = count + 1
    current = current.next

print("The number of nodes is:", count)


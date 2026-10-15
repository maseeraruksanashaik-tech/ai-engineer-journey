Python

# Day 28: Encapsulation

class Details:
    def __init__(self, name):
        self.__name = name

    def show_details(self):
        print("Name:", self.__name)

    def update_name(self, new_name):
        if new_name != "":
            self.__name = new_name
            print("Name updated successfully")
        else:
            print("Name cannot be empty")


person1 = Details("sanu")
person1.show_details()
person1.update_name("maseera")
person1.show_details()


# Example 2: Student Marks

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def show_student(self):
        print("Student marks:", self.__marks)

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks")


student1 = Student(72)
student1.show_student()
student1.update_marks(93)
student1.show_student()
student1.update_marks(937)
Python

# Day 28: Two Pointers
# Find a pair whose sum equals the target

# Example 1
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 100

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print("Pair found:", numbers[left], numbers[right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1
else:
    print("No pair found")


# Example 2
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
target = 75

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print("Pair found:", numbers[left], numbers[right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1
else:
    print("No pair found")

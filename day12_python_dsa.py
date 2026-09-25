# 1. Default argument example

def marks(subject, marks=37):
    print("subject:", subject)
    print("marks:", marks)

marks("Ai")


# 2. Default argument example - Shopping

def shopping(price, name="chain"):
    print("name of the item:", name)
    print("price:", price)

shopping(294)


# 3. Default arguments - Student Details

def student_detail(name, age, marks=393,
                   department="B.Sc. Data Science"):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

student_detail("maseera", 18)


# 4. Searching using a function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def searching_1(numbers, target=13):
    for number in numbers:
        if number == target:
            return True
    return False

print(searching_1(numbers, 8))


# 5. Another searching example using default argument

numbers = [10, 20, 30, 40, 50]

def searching_2(numbers, target=30):
    for number in numbers:
        if number == target:
            return True
    return False

print(searching_2(numbers))
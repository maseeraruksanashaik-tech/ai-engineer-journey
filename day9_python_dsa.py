# DAY 9 - Python + DSA
# Functions and Linear Search


# 1. Function Calling

def intro():
    print("Hello guys, I am Ankush")
    print("I am learning Python and DSA")
    print("My age is 20")

intro()


# 2. Adding Two Numbers

def adding_numbers():
    print(5 + 8)

adding_numbers()


# 3. Calling a Function Multiple Times

def name():
    print("Hii, my name is sanu")

name()
name()


# 4. Linear Search Using a Function

numbers = [10, 20, 30, 40, 50]

def searching_numbers(numbers, target):
    for number in numbers:
        if number == target:
            print("Found")
            return
    print("Not Found")

searching_numbers(numbers, 30)


# 5. Searching Names Using a Function

names = ["anku", "sanu", "saba", "tasleem", "neo", "sam", "niki"]

def searching_names(names, target):
    for name in names:
        if name == target:
            print("Found")
            return
    print("Not Found")

searching_names(names, "massi")
# 1. Function with parameter and argument

def country(name):
    print("I live in", name)

country("India")


# 2. Function with parameter

def intro(message):
    print("Hello everyone", message)

intro("I am Massi and I am 21 years old")


# 3. Function with two parameters

def minus(x, y):
    print(x - y)

minus(38, 12)


# 4. Searching using a function

ages = [12, 23, 42, 23, 14, 32, 24]
names = ["noor", "saba", "zara", "nafeesa"]

def searching(numbers, target):
    for number in numbers:
        if number == target:
            print("found")
            return
    print("not found")

searching(ages, 53)
searching(names, "saba")


# 5. Function with two arguments

def x(number, names):
    print("my age is", number)
    print("my name is", names)

x(18, "neo")


# 6. DSA - Linear Search for a number

numbers = [12, 25, 37, 48, 59]

def searching_number(numbers, target):
    for number in numbers:
        if number == target:
            print("found")
            return
    print("not found")

searching_number(numbers, 37)


# 7. DSA - Linear Search for a name

names = ["ankush", "neo", "javeed", "sanu", "sahil"]

def searching_name(names, target):
    for name in names:
        if name == target:
            print("found")
            return
    print("not found")

searching_name(names, "ankush")
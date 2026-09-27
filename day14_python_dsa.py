# DAY 14 - Python + DSA
# Functions: Local Variables, Global Variables, Lambda and Recursion


# 1. Local Variable

def details():
    name = "maseera"
    print(name)

details()


# 2. Global Variable

age = 26

def detail_1():
    print(age)

detail_1()


# 3. Lambda Function

subtract = lambda a, b: a - b
print(subtract(3958, 394))


# Another Lambda Example

details = lambda name: name
print(details("maseera"))


# 4. Recursion Example

def number(n):
    if n == 2:
        return

    print(n)
    number(n - 1)

number(8)


# 5. Another Recursion Example

def count(n):
    if n == 4:
        return

    print(n)
    count(n - 1)

count(6)
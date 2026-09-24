# Example of return - addition
def add(x, y):
    return x + y

result = add(28, 39)
print(result)


# Example of return - subtraction
def subtraction(a, b):
    return a - b

result = subtraction(39, 73)
print(result)


# Example of multiplication
def multiply(a, b):
    return a * b

result = multiply(83, 93)
print(result)


# Example of division
def division(x, y):
    return x / y

result = division(37, 57)
print(result)


# Example of finding whether a number is in the list
numbers = [24, 83, 73, 47, 37, 34]

def searching(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False

result = searching(numbers, 24)
print(result)


# Example of checking even or odd
numbers = [36, 57, 37, 83, 37, 638, 2]

def check_number(numbers, target):
    for number in numbers:
        if number == target:
            if number % 2 == 0:
                print("even")
            else:
                print("odd")
            return
    print("not found")

check_number(numbers, 37)


# Example of searching a name
names = ["neo", "reshma", "saleem", "sahil", "maheer"]

def checking_name(names, target):
    for name in names:
        if name == target:
            print("found")
            return
    print("not found")

checking_name(names, "majeed")
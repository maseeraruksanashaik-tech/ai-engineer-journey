# DAY 21 - Python + DSA
# Exception Handling
# try, except and continue

# Example 1: Division by zero
try:
    a = 2
    b = 0
    print(a / b)
except:
    print("You cannot divide by zero")


# Example 2: Trying to loop through an integer
try:
    number = 6

    for i in number:
        i >= 5668
        print("You can buy 3 match boxes")

except:
    print("You cannot loop through an integer")


# Example 3: Input gives a string
try:
    number = input("Enter a number = ")
    print(number + 7)

except:
    print("You must enter a number that can be used for addition")


# Example 4: Continue statement
try:
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        if i == 5:
            continue
        print(i)

except:
    print("Something went wrong")


# Example 5: Creating an error intentionally
try:
    numbers = (13, 54, 83, 82, 94, 44)

    for number in numbers:
        if number == 54:
            print(54 / 0)

except:
    print("An error occurred because we tried to divide by zero")


# Example 6: Recursion
def number(n):
    print(n)

    if n == 2:
        return

    number(n - 1)


number(8)


# Example 7: Another recursion example
def count(x):
    print(x)

    if x == 1:
        return

    count(x - 1)


count(4)
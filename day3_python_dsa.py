DAY 3 - Python + DSA

# Example of if
rupees = 47

if rupees >= 46:
    print("I can buy chocolate")

# Example of else
marks = 10000

if marks == 10004:
    print("I can pay the fees")
else:
    print("I can't")

# Example of elif
age = 21

if age <= 18:
    print("You are teenager")
elif age <= 50:
    print("You are adult")
else:
    print("Old")

# Example of searching with condition
rupees = [737, 829, 517, 37, 488, 368, 964, 356, 855, 356, 644, 786, 467]

found = False

for rupee in rupees:
    if rupee == 356:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")

# Example second - searching
marks = [17, 48, 47, 36, 37, 39, 54, 68, 97, 25, 57,
         46, 96, 58, 86, 47, 75, 97, 56, 67, 45, 75,
         78, 76, 96, 35, 86, 36, 87, 47]

found = False

for mark in marks:
    if mark == 83:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")
1. Tuple indexing
numbers = (10, 20, 30, 40, 50)

print(numbers[2])


# 2. Negative indexing
ages = (28, 97, 68, 86, 23)

print(ages[-2])


# 3. Tuple slicing
marks = (92, 7, 5746, 86, 57, 57, 79)

print(marks[1:6])


# 4. Tuple count()
marks = (289, 467, 468, 289, 648, 926, 289, 826, 837, 289)

print(marks.count(289))


# 5. Tuple index()
ages = (23, 26, 46, 26, 28, 84, 25)

print(ages.index(28))


# 6. Searching in a tuple
numbers = (2, 6, 4, 6, 28, 3, 6)

for i in numbers:
    if i == 28:
        print("Found")
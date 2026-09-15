# Example of for loop
marks = [738, 68, 67, 567, 688, 567, 865]

for mark in marks:
    print(mark)


# Example 2 - for loop with strings
cloths = ["long frock", "shorts", "pants", "jeans"]

for cloth in cloths:
    print(cloth)


# Example of range
for x in range(1, 6):
    print(x)


# Example 2 - range
for y in range(9):
    print(y)


# Example 3 - range
for a in range(2, 9):
    print(a)


# Example of while loop
age = 13

while age <= 18:
    print(age)
    age = age + 1


# Example of break
numbers = [10, 30, 89, 985, 96, 35, 86, 81, 97]

for a in numbers:
    if a == 35:
        break
    print(a)


# Example of nested loop
for i in range(1, 4):
    for j in range(2, 6):
        print(i, j)


# Example of continue
marks = [299, 87, 976, 46, 976, 578, 977, 86]

for x in marks:
    if x == 46:
        continue
    print(x)


# DSA - counting an element
names = ["zara", "sara", "mubarak", "tasleem",
         "sara", "sara", "neo", "sara"]

count = 0

for x in names:
    if x == "sara":
        count = count + 1

print(count)
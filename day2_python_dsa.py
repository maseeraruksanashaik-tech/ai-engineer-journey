# 1. Input and output
name = input("Enter your name: ")
print(name)


# 2. Type conversion - height
height = float(input("Enter your height: "))
print(type(height))


# 3. Type conversion - age
age = int(input("Enter your age: "))
print(type(age))


# 4. DSA - Traversal and searching
rupees = [278, 767, 44, 479, 356, 235, 995, 467, 754, 678, 5578, 972]

for rupee in rupees:
    if rupee == 995:
        print("found")


# 5. Searching a name
names = ["shaik", "maseera", "zara", "neo", "sam", "umar", "ankush", "jaseem"]

for name in names:
    if name == "sanu":
        print("found")
        break
else:
    print("not found")

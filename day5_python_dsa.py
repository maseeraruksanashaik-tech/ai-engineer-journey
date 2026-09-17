# 1. Indexing and Negative Indexing

numbers = [59, 96, 38, 63, 84, 29, 56, 92, 75]

print(numbers[5])
print(numbers[-5])


# 2. Slicing

marks = [84, 862, 882, 884, 567, 928, 7459, 828,
         748, 947, 983, 884]

print(marks[2:9])


# 3. append()

names = ["neo", "mohit", "shaik", "sanu"]

names.append("sara")

print(names)


# 4. insert()

numbers = [82, 86, 857, 447, 65, 877, 367, 467, 855, 865]

numbers.insert(2, 92)

print(numbers)


# 5. remove()

ages = [28, 57, 34, 45]

ages.remove(57)

print(ages)


# 6. pop()

marks = [828, 97, 278, 366, 872, 863]

marks.pop(1)

print(marks)


# 7. len()

marks = [837, 857, 468, 467, 4678, 856, 865,
         8668, 866, 876, 86689, 5678, 5785,
         356, 24, 488, 6986, 757, 8855, 886278,
         6876, 7578, 7577]

print(len(marks))


# 8. DAY 5 CHALLENGE

numbers = [10, 20, 30, 40, 50]

numbers.pop(2)
numbers.insert(2, 100)

print(numbers)
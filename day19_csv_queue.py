# DAY 19 - Python
# CSV File Handling

import csv

# Writing student data
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "age", "class", "marks"])
    writer.writerow(["shaik", 14, 8, 748])
    writer.writerow(["ankush", 20, 389])
    writer.writerow(["sanu", 18, 379])

# Reading student data
with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Writing shopping data
with open("shopping.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["dress", "color", "price"])
    writer.writerow(["kurti", "black", 848])
    writer.writerow(["long dress", "brown", 738])

# Reading shopping data
with open("shopping.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
# DAY 19 - DSA
# Queue using Python

queue = []

queue.append("nabiya")
queue.append("saba")
queue.append("reshma")

print(queue)

removed = queue.pop(0)

print("Removed:", removed)
print(queue)

queue.append(18)

print(queue)
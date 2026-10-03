# DAY 20 - Python + DSA
# JSON and Linked List

# =========================
# JSON
# =========================

import json

shopping_list = {
    "dress": "long dress",
    "shoes name": "nick",
    "price": 1949,
    "color": "pink"
}

with open("shopping_list.json", "w") as file:
    json.dump(shopping_list, file)

with open("shopping_list.json", "r") as file:
    data = json.load(file)
    print(data)


student_marks = {
    "sara": 388,
    "nabiya": 538,
    "reshma": 384,
    "sabira": 484,
    "ankush": 943,
    "sanu": 832,
    "majeed": 383,
    "maheer": 494,
    "maseera": 938
}

with open("student_marks.json", "w") as file:
    json.dump(student_marks, file)

with open("student_marks.json", "r") as file:
    data = json.load(file)
    print(data)


# =========================
# DSA - Linked List
# =========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(40)
node3 = Node(60)

node1.next = node2
node2.next = node3

current = node1

while current is not None:
    print(current.data)
    current = current.next
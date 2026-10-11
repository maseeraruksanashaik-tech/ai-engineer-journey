Python
class Person:
    def __init__(self, name, age, occupation, salary):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary

    def display(self):
        print("name=", self.name)
        print("age=", self.age)
        print("occupation=", self.occupation)
        print("salary=", self.salary)


person1 = Person("ankush", 20, "software engineer", 37000)
person1.display()


class Sales:
    def __init__(self, name, total_budget, ad, final_profit, loss):
        self.name = name
        self.total_budget = total_budget
        self.ad = ad
        self.final_profit = final_profit
        self.loss = loss

    def display(self):
        print("name=", self.name)
        print("total budget=", self.total_budget)
        print("ad=", self.ad)
        print("final profit=", self.final_profit)
        print("loss=", self.loss)


sales1 = Sales("sara", 638384893, 9374, 5367383, 73838292)
sales2 = Sales("maseera", 637389339, 73838, 73728, 9384748)
sales3 = Sales("unesa", 638282, 8382892, 52728, 72829)
sales4 = Sales("ankush", 7383992, 8392992, 929292, 9382)

sales1.display()
sales2.display()
sales3.display()
sales4.display()
Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4

# Traversing the linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next

# Searching for 30
target = 30
current = node1
found = False

while current is not None:
    if current.data == target:
        found = True
        break
    current = current.next

if found:
    print("found")
else:
    print("not found")
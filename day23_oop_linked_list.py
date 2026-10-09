Writing
# DAY 23 - Python + DSA
# OOP Constructors and Linked List

# Example 1: OOP - Soap
class Soap:
    def __init__(self, name, price, expiry_date):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date

    def display(self):
        print("Soap name =", self.name)
        print("Soap price =", self.price)
        print("Expiry date =", self.expiry_date)


soap1 = Soap("no.1", 10, "28/12/2026")
soap1.display()


# Example 2: OOP - Car
class Car:
    def __init__(self, name, amount, warranty):
        self.name = name
        self.amount = amount
        self.warranty = warranty

    def display(self):
        print("Name of the car =", self.name)
        print("Amount of car =", self.amount)
        print("Warranty of car =", self.warranty)


car2 = Car("thar", 63939, 2078)
car2.display()


# Example 3: DSA - Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(40)
node3 = Node(60)

# Connect the nodes
node1.next = node2
node2.next = node3

# Traverse and print the linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next


# Example 4: Constructor with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("maseera", 18)

print(person1.name)
print(person1.age)
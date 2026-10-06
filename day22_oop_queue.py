# DAY 22 - Python + DSA
# OOP Basics + Queue

# Example of OOP

class Tree:
    pass


tree2 = Tree()
tree2.color = "green"
tree2.height = 5.2
tree2.flower_color = "pink"

print("Tree color =", tree2.color)
print("Tree height =", tree2.height)
print("Flower color =", tree2.flower_color)


# Another example

class Bus:
    pass


bus1 = Bus()
bus1.ticket = 5898
bus1.ac = "available"
bus1.days = "two days"
bus1.food = "arranage"

print("Ticket price =", bus1.ticket)
print("AC =", bus1.ac)
print("Trip days =", bus1.days)
print("Food =", bus1.food)


# Another example

class HouseConstruction:
    pass


house3 = HouseConstruction()
house3.length_of_area = "one acre"
house3.steps = 3
house3.total_price = 4749936227

print("Length of area =", house3.length_of_area)
print("Steps =", house3.steps)
print("Total amount =", house3.total_price)


# Example of Queue

queue = []

queue.append("neo")
queue.append(22)
queue.append("sara")
queue.append("shaik")
queue.append(8494)

print(queue)

# FIFO: First In, First Out
queue.pop(0)

print(queue)
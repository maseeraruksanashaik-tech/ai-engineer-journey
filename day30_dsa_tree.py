Python

# Day 30 - DSA: Tree Basics

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example 1: Tree with names
root = Node("sanu")
root.left = Node("ankush")
root.right = Node("neo")

print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)

# Example 2: Tree with numbers
root2 = Node(21)
root2.left = Node(18)
root2.right = Node(22)

print("Root:", root2.data)
print("Left child:", root2.left.data)
print("Right child:", root2.right.data)

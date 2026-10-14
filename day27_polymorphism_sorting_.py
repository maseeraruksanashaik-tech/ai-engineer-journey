Python

# Day 27: Example 1 - Polymorphism

class Human:
    def sound(self):
        print("Human can talk")


class Animals:
    def sound(self):
        print("Animals can bark, meow, etc.")


human1 = Human()
animals1 = Animals()

human1.sound()
animals1.sound()


# Example 2 - Polymorphism

class Mom:
    def said(self):
        print("Have you completed your work?")


class Child:
    def said(self):
        print("Yes, Mom!")


mom1 = Mom()
child1 = Child()

mom1.said()
child1.said()
 dsa

# Day 27: Example 1 - Ascending and Descending Sorting

marks = [48, 494, 649, 37, 29, 293, 537, 3637, 378]

marks.sort()
print("Ascending order:", marks)

marks.sort(reverse=True)
print("Descending order:", marks)


# Example 2 - Descending Sorting

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.sort(reverse=True)
print("Descending order:", numbers)



# Example of *args

def numbers(*items):
    for item in items:
        print(item)

numbers("pen", "cryans", "books", "pad", "phone", "charger")


# Another example of *args

def shopping(*things):
    for thing in things:
        print(thing)

shopping("bag", "bedsheet", "chair", "bed", "pillow")


# Example of **kwargs

def shopping_1(**things):
    for key, value in things.items():
        print(key, "=", value)

shopping_1(
    name="ankush",
    department="bsc.data science",
    age=93
)


# Another example of **kwargs

def price(**things):
    for key, value in things.items():
        print(key, "=", value)

price(
    pens=43,
    pad=479,
    phone=48948,
    chair=578
)


# DSA - Searching with a function

numbers = [29, 78, 97, 96, 296, 57, 97, 57]

def searching(*numbers):
    for number in numbers:
        if number == 296:
            print("found")
            return
    print("not found")

searching(*numbers)
# DAY 15 - Python + DSA
# List Comprehension and Dictionary Comprehension


# 1. List comprehension
number = [x for x in range(2, 9)]
print(number)


# 2. Another list comprehension
number = [i for i in range(1, 6)]
print(number)


# 3. Cube using list comprehension
numbers = [3, 5, 7, 9, 14, 17, 20]

cube = [number * number * number for number in numbers]
print(cube)


# 4. Showing even numbers
numbers = [3, 8, 11, 14, 17, 20]

even = [number for number in numbers if number % 2 == 0]
print(even)


# 5. Filtering numbers less than or equal to 100
numbers = [
    14, 83, 86, 97, 948, 367, 8554, 6657,
    256, 87, 77, 78, 86, 886, 8869, 65
]

numbers = [number for number in numbers if number <= 100]
print(numbers)


# 6. Dictionary comprehension
numbers = [1, 9, 47, 9, 57, 97, 5, 8, 5, 9, 6, 9, 4, 9, 3, 9, 8]

squares = {number: number * number for number in numbers}
print(squares)
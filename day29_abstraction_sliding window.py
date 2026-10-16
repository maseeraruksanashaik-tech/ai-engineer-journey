Python

# Day 29: Python Abstraction

from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def information(self):
        pass


class LinesBook(Book):
    def information(self):
        print("Madam said to use a lines book for English")


class ShortBook(Book):
    def information(self):
        print("Use a short book for homework")


class BroadLinesBook(Book):
    def information(self):
        print("Hindi madam said to use a broad lines book")


lines_book = LinesBook()
short_book = ShortBook()
broad_lines_book = BroadLinesBook()

lines_book.information()
short_book.information()
broad_lines_book.information()

dsa

# Day 29: DSA - Sliding Window

# Example 1: Window size 2
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
window_size = 2

print("Window size 2:")
for i in range(len(numbers) - window_size + 1):
    total = sum(numbers[i:i + window_size])
    print(total)


# Example 2: Window size 4
marks = [739, 934, 9393, 538, 538, 548]
window_size = 4

print("Window size 4:")
for i in range(len(marks) - window_size + 1):
    total = sum(marks[i:i + window_size])
    print(total)

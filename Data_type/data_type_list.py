# Value stored in particular memory location with formate [] its considered as list.
# List is collection data type, it can have zero or n number of objects
# List are mutable
# List is collection of homogenising and heterogeneous objects
# List is ordered
from copy import deepcopy
from operator import index

# Creation of list
a = list()
print(a)  # Built-in function returns empty list
b = []
print(b)

# Built-in function take sequence and create a list
a = list("hello")
print(a)  # ['h', 'e', 'l', 'l', 'o']

# len() is a built in function gives the length of collection data type
print(len(a))  # 5

# int, float, bool and None to list(we cannot convert individual data to list, but string can
# a = 10
# a = 10.0
# a = True
# a = None
# print(list(a)) # Get TypeError since int is not a sequence

# String to list
a = "hello"
print(list(a))  # ['h', 'e', 'l', 'l', 'o']

# Tuple to string
a = (1, 2, 3)
print(list(a))  # ['h', 'e', 'l', 'l', 'o']

# Dictionary to string
a = {"apple": 1, "mango": 3}
print(list(a))  # ['apple', 'mango'] take kye and create list

# Set to list
a = {1, 2, 3}
print(list(a))  # [1, 2, 3]

# List indexing is extracting the elements from the list
a = [1, 2, 3, 4]
print(a[1])  # 2
print(a[0])  # first element 1
print(a[-1])  # last element 4

# Slicing is extracting multiple objects from a list return string only
print(a[::-1])  # [4, 3, 2, 1]
print(a[0:3])  #  [1, 2, 3]

# Built-in function
print(dir(a))  # Give all attributes attached to specified object

# append() used to add the item at the end
a.append(5)
print(a)  #  [1, 2, 3, 4, 5]

a.append([6])
print(a)  # [1, 2, 3, 4, 5, [6]]

a.append((1,))
print(a)  # [1, 2, 3, 4, 5, [6], (1,)]

# Extend existing list with the sequence
a = [1, 2, 3, 4, 5]
a.extend([6,7])  #  [1, 2, 3, 4, 5, 6, 7]
print(a)

a.extend((8,9))
print(a)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop() removed the specified elements from the list and return the removed element
# By default it remove the last element
print(a.pop())  # 9
print(a.pop(0))  # First element 1

# clear() clear the all elements, but not delete the list
b = [3,4,5,6]
b.clear()
print(b)

# copy() copy the elements of the list
c = a.copy()
print(c)

# Shallow copy and deepcopy
# whenever we copy the list , new list will be created and both have different memory location,
# but nested list will be shared along with the both the list
a = [1,2,3,[1,2]]
b = a.copy()
print(b)
print(id((a))) # Stored in different memor location
print(id(b))  # Stored in different memor location

print(id(a[3])) # Both are in same location
print(id(b[3])) # Both are in same location

b[3].append(1)
print(a) # Changes showed in both the list
print(b)  # Changes showed in both the list

# Deepcopy
# whenever we copy the list , new list will be created and both have different memory location,
# also nested list will be stored in different location

a = [1,2,3,[1,2]]
b = deepcopy(a)
print(id(a[3])) # Both are in different location
print(id(b[3])) # Both are in different location

# sort() sort the list
a = [1,2,3,23,20]
a.sort()  # by default sort in ascending order
print(a)  # [1, 2, 3, 20, 23]

# list should be homogeneous
# a = [1,2,3,23,20,"s"]
# a.sort()  # return type error

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

# sorting by the length
words = ["apple", "banana", "kiwi", "grape"]
words.sort(key=len)
print(words)


numbers = [-10, 5, -2, 3]
numbers.sort(key=abs)
print(numbers)  # ignore even it is negative

words = ["Banana", "apple", "cherry"]
words.sort(key=str.lower)
print(words)  # Output: ['apple', 'Banana', 'cherry'] convert to lower and sort

words = ["apple", "banana", "cherry"]
words.sort(key=lambda word: word[-1])
print(words)  # sorting based on the last word

# Sorting a List of Tuples (By a Specific Index)
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda student: student[1])  # Sort by age (index 1)
print(students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Sorting a List of Dictionaries
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]
students.sort(key=lambda student: student["age"])

# Sorting in Reverse Order
numbers = [5, 2, 9, 1]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 2, 1]


#  Sorting with Custom Functions
def custom_sort(value):
    return value % 3  # Sort based on remainder when divided by 3

numbers = [10, 3, 7, 6, 2]
numbers.sort(key=custom_sort)
print(numbers)  # Output: [3, 6, 10, 7, 2]

# Sorting with Multiple Criteria
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23), ("Bob", 19)]
students.sort(key=lambda student: (student[0], student[1]))  # Sort by name, then age
print(students) # [('Alice', 25), ('Bob', 19), ('Bob', 20), ('Charlie', 23)]

# index() returns the index of specified object in the list
numbers = [10, 3, 7, 6, 2,6,6]
print(numbers.index(2))

# count() return the count of specified object in the list
print(numbers.count(6))

# remove the element based on the index
print(numbers.pop(0))  # 10 or its remove the last element

# remove()
numbers.remove(6)
print(numbers)

# insert() specified position
numbers.insert(0, 20)
print(numbers)

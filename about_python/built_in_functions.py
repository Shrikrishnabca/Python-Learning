# Python has set of built-in function, we don't need to import use the built-in function
# We have set of function implemented in python, we can use those function that will reduce the execution time

# abs() - Returns the absolute value of the number
a = -10
positive_result  = abs(a)
print(positive_result)

# all() - Returns True if all the items are True in an iterable
# Write a program to check all result are True
result_1 = True
result_2 = True
result_3 = True
final_result = all([result_1, result_2, result_3])
print(final_result)

# any() - Returns True if all the items are True in an iterable
result_1 = False
result_2 = True
result_3 = False
final_result = any([result_1, result_2, result_3])
print(final_result)

# bool() - returns the boolean value of the specified value
# Integer value to boolean
# Integer positive or negative int is True except 0
print(bool(1))
print(bool(-1))

# Integer 0 is False
print(bool(0))

# Floating value
# all positive or negative floating number is True
print(bool(0.009))
print(bool(1.00))
print(bool(-0.009))
print(bool(-1.00))

# Floating value 0 is False
print(bool(0.00))

# default value of bool() is False
print(bool())

# char() - convert and return Unicode to character
print(chr(56))

# Raise value error if Unicode was wrong
# print(chr(9446777))

# dict() - returns and convert to dictionary
print(dict())
# convert list of tuple to dictionary
print(dict([(2,3),(5,6)]))

# enumerate() - returns list of tuple having index value amd item
my_list = ["krishna", "madhu", "naga","raki"]
for i, value in enumerate(my_list):
    print(i, value)

# filter() - filter the iterator using specified function if function return true pic the item
# it will accept specified function returns True
my_list = [1,2,3,4,5,6,7,8,9]
def is_even(number):
    if number % 2 == 0:
        return True

print(list(filter(is_even, my_list)))

# float() - returns floating value
# default value of float is 0.0
print(float())

# Integer to float
int_val = 10
print(float(int_val))  # 10.0

# Bool to float True--->1.0
print(float(True))  # 1.0
# False---> 0.0
print(float(False))  # 0.0

# id() - returns the memory location id
a = 10
b = 20
c = a
print(id(a))
print(id(b))
print(id(c))

# input() To take user input dynamically during the run time
# If we give input in any formate its return type is string
# name = input("Enter your name")
# print(f"Hello {name}")

# int() - return integer number
# Default value is 0
print(int())
# float to int
print(int(3.0004))
# boolean to int
print(int(True))
print(int(False))

# isinstance() - return True if specified object and specified data type are same
# True and False are instance of bool built in class as well as integer built in class
# integer class is a super class for boolean class

# bool
print(isinstance(True, int))
print(isinstance(False, int))
print(isinstance(True, bool))
print(isinstance(False, bool))

# int
print(isinstance(0, int))
print(isinstance(10, int))
print(isinstance(-10, int))

# float
print(isinstance(0.0, float))
print(isinstance(10.00, float))
print(isinstance(-10.00, float))

# len() - returns number item in a sequence
# index start from 0 len starts from 1
my_list = [1,2,3,4,5,6]
emp_list = []
print(len(my_list))
print(len(emp_list))

# list() return list
# default value is empty list
a_list = list()
print(a_list)

# string to list
name = "shrikrishna"
name_char = list(name)
print(name_char)

# set to list
a_set = {1,2,3}
print(list(a_set))

# tuple to list
a_tuple = (1,2,3,)

# dict to list (takes key only)
a_dict = {"s": 1, "b": 2}
print(list(a_dict))

# map() - map function execute specified function for all item in an iterable
# map the function with items in an iterable

def myfunc(n):
    return len(n)
may_fruit = ['apple', 'banana', 'cherry']
result = map(myfunc, may_fruit)
print(list(result))

# we can give n numbers of iterable but that many parameters we have to declare in header
def add_two_list(_a: iter, _b: iter):
    return a + b
a = [1,2,3]
b = [3,2,1]
result = map(add_two_list, a, b)

# max() - returns max item in a sequence
a_list = [2,4,5,6,3,10,3,4]
print(max(a_list))
print(max(5, 10,20,30,12,55))
# Return the name with the highest value, ordered alphabetically
print(max(["nagraj", "madhu", "krishna"]))

# min() - returns minimum item in a sequence
print(min(a_list))
print(min(12,3,1,-1))
# Return the name with the lowest value, ordered alphabetically
print(min(["nagraj", "madhu", "krishna"]))

# open() - function opens the file in specified mode and returns an file object
# Opening a file in read mode raises error if file not existed
# file_obj = open("names.txt", "r")
# Opening the file in write it will create file if it not exists
# if you create new instance for the same file it will overwrite
file_obj = open("names.txt", "w")
file_obj.write("helllo")
file_obj = open("names.txt", "w")
file_obj.write("krishna")
# Opening the file in append it will create the file if it's not exist
## if you create new instance for the same file it will overwrite
file_obj = open("names.txt", "a")
file_obj.write("helllo")
file_obj = open("names.txt", "a")
file_obj.write("krishna")
# Opening the file in create , it will return the error if file exists
# file_obj = open("names_.txt", "x")

# ord() - convert the character to corresponding Unicode
print(ord("h"))

# print() - builtin function to print output on the console
print("Hello shri krishna")
print("i am ", "shri krishna", sep="******")
print("krishna", end='\n')

# range() - return the sequence of number
# starting from 0 and increased by 1 by default
# range(start, end, step_count)
for _ in range(2):
    print("hello")
for _ in range(0, 11, 2):
    if _ != 0:
        print(_)
for _ in range(1, 11, 2):
    print(_)

# reversed() - returns the reversed iterator
my_list = [2,3,4,5,6,7]
print(list(reversed(my_list)))
# we cannot reverse the set since they un ordered
# my_set = {1,2,3,4,5,6}
# print(set(reversed(my_set)))
my_tuple =(1,2,3,4,5)
print(list(reversed(my_tuple)))
my_name = "shri krishna"
print(list(reversed(my_name)))
my_dict = {"s": 1, "a": 2}

# round() - round the floating number and return integer number
# we can also give value to decide how many decimal values are needed
print(round(1.222,3))

# set() return set
# default value of set is empty set set(), you cannot use {} to create an empty set
# if we convert to set every time order changes since its unordered
print(type({1}))
print(set())
# list to set
my_list = [1,2,3,5,4]
print(set(my_list))
# dictionary to set
my_dict_ = {"s": 1, "a": 2, "d": 3}
print(set(my_dict_))
# string to set
my_name = "shri krishna"
print(set(my_name))
# tuple to set
my_tuple =(1,2,3,4)
print((set(my_tuple)))

# sorted() returns the sorted list
# default sort in ascending formate
# sorted(iterable, key=key, reverse=reverse)
# if you want descending you have to give reverse as True
print(sorted(my_list, reverse=True))
# orders the name lower length to hig
names = ["shri krishna", "naga", "madhu"]
print(sorted(names, key=len))

# execute the function based on the result sort the specified list
# write a program to print closest number 10
def my_func(n):
    return abs(10-n)
new_list = [1, 12, 3, 32]
print(sorted(new_list, key=my_func)) # [9, 2, 7, 22]----> [12, 3, 1, 32]

# str() returns the string obj
# default value is empty string
# str(object, encoding=encoding, errors=errors)
print(str(3.5))
print(str(my_dict))
print(str(my_list))
print(str(my_tuple))
print(str({1,2,3}))

# sum() returns the sum of iterable
# sum(iterable, start) we can give the start value that well be added to return value
print(sum(my_list))  # 15
print(sum(my_list, 10))  # 25

# tuple() returns the tuple
# empty tuple ()
print(tuple())
# tuple with one object
print(tuple([1]))  # (1,) else its considered as integer value
# list to tuple
print(tuple([1,2,3]))  # (1,2,3)
# dictionary to tuple
print(tuple({"s":1,"b":2}))  # ("s", "b")
# set to tuple
print(tuple({1,2,3}))  # (1,2,3)
#string to tuple
print(tuple("hello"))  # ('h', 'e', 'l', 'l', 'o')

# type() returns the type of data
print(type(my_dict_))  # <class 'dict'>
print(type(my_tuple))  # <class 'tuple'>
print(type(my_name))   # <class 'str'>

# zip() the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together
# tuple of paired object
# if size are different it ignores the extra objects
a = ("John", "Charles", "Mike",)
b = ("Jenny", "Christy", "Monica", "hello")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(list(x))

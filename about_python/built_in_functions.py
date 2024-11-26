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






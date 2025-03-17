# Operators are used to perform some operation on operands, we have same mathematical operators in python

# Addition
a = 10
b = 20
print(f"Addition of a and b is {a + b}")

# Subtraction
print(f"Subtraction of a nad b is {a - b}")

# Multiplication
print(f"Multiplication of a nad b is {a * b}")

# Division
# it gives a floating result if you want to use below logic
print(f"Division of a and b is {b / a}")  # 2.0
print(f"Division of a and b is {b // a}")  # 2 flor division

# Modules returns the reminder
print(f"Reminder of a and b division is {b % a}")

# Exponentation(power of)
print(f"{a} to the power {b} is {a ** b}")

# Assignment operators '=' used to assigning a value
a = 10
a += 1  # Addition assignment operator its equivalent to a = a + 1
a -= 1  # Subtraction assignment operator its equivalent to a = a - 1
a *= 1  # Multiplication assignment operator its equivalent to a = a * 1
a /= 1  # Division assignment operator its equivalent to a = a / 1

print(a)

# == is used to check both the values or same or not (returns boolean value)
print(a == b)  # 10 == 20

# != not equal
print(a != b)

# > greater than (returns boolean value)
print(a > b)  # 10 > 20

# >= greater than or equal
print(100 >= 20)
print(100 >= 100)

# < less than (returns boolean values)
print(a < b)  # 10 < 20

# <= less than or equal to
print(100 <= 200)
print(200 <= 200)

# logical operator
# and true if both the condition true and else false
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or true if one of the condition true , if both false returns
print(True and True)  # True
print(True and False)  # True
print(False and True)  # True
print(False and False)  # False

# not vise versa
print(not True)  # False
print(not False)  # True

# Identity and Membership Operators
c = [1, 2, 3]
d = c
e = [1, 2, 3]

# is return true variable address are same
print(c is d)  # True
print(c is e)  # False
print(c == d)  # False
print(c == e)  # True

# in check object in collection
print(1 in c)  # True
print(4 in c)  # False

# not in
print(4 not in c)  # True
print(1 not in c)  # False

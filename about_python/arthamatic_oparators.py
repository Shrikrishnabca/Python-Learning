"""Module for arithmetic operators"""

# Addition: " + "
print(5 + 2)  # 7

# Subtraction: " - "
print(5 - 2)  # 3

# Multiplication: " * "
print(5 * 2)  # 10

# Division: " / "
print(5 / 2)  # 2.5

# Floor Division: " // " Give integer results
print(5 // 2)  # 2

# Modulus: " % " Returns the remainder of division
print(5 % 2)  # 1

# Exponentiation: " ** " Raises the first value to the power of the second
print(5 ** 2)  # 25


# Relational operators, Gives boolean value
# Equal to: " == " Checks if two values are equal
print(5==5)  # True

# Not equal to: " != " Checks if two values are not equal
print(3!=4)  # True

# Greater than: Checks if left value is greater than right
print(5>3)  # True

# Less than: Checks if left value is less than right
print(3<5)  # True

# Greater than or equal to: Checks if left value is greater than or equal to right
print(5>=5)  # True
print(5>=6)  # True

# Less than or equal to: Checks if left value is less than or equal to right
print(3<=3)  # True
print(2<=3)  # True

# Identity operators in Python are used to compare the memory addresses of two objects.
a = "Hello"
b = a
print(b is a) # Returns True if both variables refer to the same object
c = "hello"
print(c is not a)  # Returns True if both variables do not refer to the same object

# Membership operators in Python are used to test whether a value is present in a sequence
# (such as a list, tuple, string, or dictionary) or not

print(a in "hello good morning asha")  # Returns True if the specified value is found in the sequence

print(a not in "hello good morning")  # Returns True if the specified value is not found in the sequence




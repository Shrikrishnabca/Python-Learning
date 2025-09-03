# Exception is an error that occurred during the runtime

# Exception Name    ------------ What It Means
# ZeroDivisionError	------------ Division by zero
# ValueError	    ------------ Invalid value (e.g., int("abc"))
# TypeError	        ------------ Invalid type operation (e.g., 3 + "abc")
# IndexError	    ------------ Index out of range in list
# KeyError	        ------------ Dictionary key not found
# FileNotFoundError	------------ File doesn’t exist
# AttributeError	------------ Attribute/method doesn’t exist
# ImportError	    ------------ Can’t import module

# Exception handling is a way to detect, respond to, and recover from errors that occur
# while your program is running

# syntax:
# try:
#     # Code that might raise an exception
#     risky_code()
# except SomeError:
#     # What to do if error happens
#     print("Something went wrong")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Full Form with else and finally
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Not a valid number")
else:
    print("Result is", result)
finally:
    print("This runs no matter what!")

# Customer exception is user defined error
# You create it when you want to raise specific, meaningful errors in your own application logic.
# It helps you make your code more readable, structured, and easier to debug.

# You define a custom exception by inheriting from the built-in Exception class.
class MyCustomError(Exception):
    pass

raise MyCustomError("Something went wrong!")




# Function is a block of code to perform specific task, Functions are get executed once its called
from typing import Tuple, List, Dict

from about_python.built_in_functions import result


# def - is keyword to define the function
# We can pass multiple values to the function, while calling it.
# Parameter is a variable use in a function definition to accept values when the function is called

# Argument: is the value you pass to function when you call it.
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}")
greet("Alice")  # "Alice" is an argument


# Types of arguments in python
# 1. Positional arguments: value are passed in the order as parameter declared in function header
def add(a, b):
    return a + b
add(5, 3)  # 5 is passed to a, 3 to b

# 2. Keyword arguments: Value are passed by the name
add(a=3, b=2)

# 3. Default argument: if you dont pass the value , default value is used
def greet(name="shri krishna"):
    print(f"helo {name}")

# 4. Variable length positional argument: accept multiple positional arguments as tuple
def greet(*names):
    print(f" Hello to {name}")

# 5. variable length keyword argument: Accept the multiple keyword argument as a dictionary
def show_detail(**data):
    print(data)
show_detail(name="shri krishna", age=26)

# 6. Positional only argument: is a function parameter that should be passed as positional argument, not by name
# We can define them using a "/"
def func(a, b, /, c, d):
    pass
# here a and b are positional only
# c and d can be positional or keyword

# 7. Keyword only argument: is function parameter that should be passed as keyword.
# We define them using "*"
def func(a,b, *, c, d):
    pass
# here c and d should be keyword argument
#  a and b can be anything

# Type hinting let you specify the expected data type of function arguments and return value
# Function with string return
def greet(name: str) -> str:
    return f"Hello, {name}"


# List as input
def total(numbers: List[int]) -> Dict[str, int]:
    return {"Sum": sum(numbers)}


# Tuple
def coordinate() -> Tuple[float, float]:
    return (1.2, 34.2)

# Types of functions
# 1. Built-in function are already available in python
# Examples: print(), len(), type(), sum(), input()
print("Hello krishna")
print(len("Python"))

# 2. User defined function: User created function using def
def great(name: str):
    print(f"Hello good morning {name}")

# 3. Lambda(Anonymous) function: these are small anonymous function, defined using the lambda keyword
# its used when you need simple function for a shorter period of time-especially for operations like
# filtering, mapping, or sorting.
# syntax: lambda arguments: expression
add = lambda a, b: a + b
print(add(1,2))

# map
nums = [1,2,3]
result_ = list(map(lambda x: x * x, nums))
print(result_)

# filter
nums = [1,2,3,4]
result_ = list(filter(lambda num: num % 2 == 0, nums))
print(result_)

# Sorted
people = [("Alice", 25), ("Bob", 22), ("Charlie", 30)]
print(sorted(people, key= lambda x: x[1]))

# Recursive function: function that calls its self
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
print(factorial(5))

# nested function are function defined inside another function
def outer():
    def inner():
        print("inner")
    return inner

# Higher-Order Functions
# Takes a function as an argument or returns one
def shout(text):
    return text.upper()

def _greet(func):
    return func("hello")

print(_greet(shout))  # Output: HELLO

# 7. Generator Functions: is special function that yield value one at a time, pausing after each value
# instead of returning all at once

# Return:
# return key word is used to return the value back to the calling function, once it reach the return
# keyword control will go out of the function

# Yield:
# yield is keyword used return the value back to the function and pause the execution

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Async Functions: Used with asynchronous programming (async/await keywords).
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

arr = [2, 10, 7, 3, 6]
# target=5
# result = set()
# for i in arr:
#     for j in arr:
#         if i + j == target:
#             result.add(i)
#             result.add(j)
# print(result)

arr.sort()
arr = [2, 2, 3, 7, 10]
target = 5


def two_sum(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        tot = arr[low] + arr[high]
        if tot > target:
            high -= 1
        elif tot < target:
            low += 1
        else:
            return arr[low], arr[high]


print(two_sum(arr, target))



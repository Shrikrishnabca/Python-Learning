# A decorator is a function that wraps another function, to add extra functionality before or after it runs.
# Decorators are the function which add extra functionality to the function without modifying the function
import time


def my_decorator(func):
    def wrapper():
        print("starting the decorator function")
        func()
        print("Ending the decorators")
    return wrapper

@my_decorator
def my_func():
    print("Executing my function")

my_func()

# starting the decorator function
# Executing my function
# Ending the decorators

def timer(func):
    def wrapper(name):
        print("start counting the time")
        start = time.time()
        func(name)
        end = time.time()
        print(f"Function took {end-start} for execution")
    return wrapper

@timer
def great(name):
    print(f"Good morning {name}")
    time.sleep(1)
    print(f"Good night {name}")

great("shrikrishna")

# start counting the time
# Good morning shrikrishna
# Good night shrikrishna
# Function took 1.0005364418029785 for execution

def greet(name):
    print(f"Hello, {name}!")

# You can't directly decorate this unless wrapper accepts arguments:

def great_decorator(func):
    def wrapper(*args, **kwargs):
        print(">> Before")
        func(*args, **kwargs)
        print(">> After")
    return wrapper

@great_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("shrikrishna")


# Common Built-in Decorators
# Decorator	Purpose
# @staticmethod	Define method not tied to class instance
# @classmethod	Define method tied to class, not instance
# @property	Make method accessible like an attribute
# @functools.wraps	Preserve metadata (name, docstring)
# A method is a function defined inside a class that acts on the objects (instances) of that class.
class Myclass:

    def my_function(self):
        print("executing my function")

my_class = Myclass()
my_class.my_function()

# type:
# Instance Method
# works with object instance
# self is the first parameter
# From the instance method we can access instance variable and class variable
# self is a keyword which holds the current instance

class TataCar:
    brand = "Tata"
    def __init__(self,speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} is now going {self.speed} km/h")

car1 = TataCar(60)
car1.accelerate()  # Tata is now going 70 km/h

# Class Methods
# affects class
# Takes cls as a first argument
# marked as @classmethod
# handles the shared data
# we can have access to class variable

class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def how_many(cls):
        print(f"We have {cls.count} students.")

s1 = Student("Asha")
s2 = Student("Ravi")
Student.how_many()  # We have 2 students.

# Static Methods
# normal function inside a class without access to any data
# Marked with @staticmethod
# Function logically belongs to the class. But doesn’t need object/class data

class Math:
    @staticmethod
    def square(x):
        return x * x

print(Math.square(7))  # 49
print(Math().square(7))  # 49







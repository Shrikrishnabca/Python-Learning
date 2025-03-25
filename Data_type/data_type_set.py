# Sets are un-ordered , not allow duplicate element
# Allow homogeneous and heterogeneous objects
# Set is mutable

# Creating a set
a= {1,2,3}
print(a)

b= set()
print(b)  # Empty set: set()

c = {}
print(type(c))  # Considered as dictionary

d = {1}
print(type(d))  # Considered as set

# Remove the duplicate values automatically
a = {1,2,3,1,2,3}
print(a)

# True and 1 is considered the same value:
print({1,True, 0, False})

# len()
print(len(a)) # 3

# homogeneous elements
a = {1,2,3}
b = {True, False, False}
c = {"apple", "banana", "apple"}

# Heterogeneous
d = {True, 1, "apple"}  # {True, 'apple'}
print(a)

# In case of True and 1 first one considered and second one will be ignored
print({1, True})  # {1}
print({True, 1})  # {True}

# set allow only hash object, object has __hash__ magic method , immutable objects are hash value

# class MyClass:
#     def __init__(self, value):
#         self.value = value  # Mutable attribute
#
#     def __hash__(self):
#         return hash(42)  # Fixed hash value
#
#     def __eq__(self, other):
#         return isinstance(other, MyClass) and self.value == other.value
#
#
# obj1 = MyClass(10) # obj1 is hash object since __hash__ is override
# obj2 = MyClass(20)
#
# print(hash(obj1))  # ✅ Works
# print(hash(obj2))  # ✅ Works (same hash as obj1)
#
# # But we can still mutate obj1:
# obj1.value = 50  # ✅ Allowed, even though the object is hashable

# Built-in functions
# union()
a = {1,2,3}
b = {3,4,5}
print(a.union(b))  # {1, 2, 3, 4, 5} all elements ignore duplicates

print(a.intersection(b))  # {3} common element

print(a.difference(b))  # {1,2}

print(a.symmetric_difference(b))  # {1,2,4,5} only unique

# Adding the element
a = {1,2,3}
a.add(4)  # take one object
print(a)  # 1, 2, 3, 4}

a.update([4,5,6])  # take iterable
print(a)  #  {1, 2, 3, 4, 5, 6}

# Removing the elements
a = {1,2,3}
print(a.pop()) # remove the random element and it returns

# Removing specific element
a = {1,2,3}
a.remove(1)
print(a)  # {2, 3}

# Clear the all element
a.clear()
print(a)  # set()





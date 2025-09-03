"""Module for scope in python"""

# Whatever we created inside the function is considered as local scope, the "a" declared outside will
# be in global scope
# "a" outside is different and "a" inside function is different
a = 1
def modify_a():
    a = 2
    print(a) # 2
print(a) # 1
modify_a()
print(a) # 1

# In python has no block scope
b = 2
for i in range(2):
    a = 1
print(b, a)

# Accessing the global scope element
a = 10
def modify_a():
    global a
    a += 1
    print(a)
modify_a()
print(a)

# Global constants - convention is never change in future
PI = 3.1459
GOOGLE_URL = "https://www.google.com/"

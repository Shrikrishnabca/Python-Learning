"""Module for string formating"""
# String formating in python allow you to insert a variable into string

# 1. String formating using f string
name = "shri krishna"
age = 25
print(f"Hello {name} you are {age} old")

# 2. String formating using formate() function
print("Hi {}, you are {} old".format(name, age))

# 3. String formating using operators
# Formate specifier
# %s ---> string
# %d -----> int
# %f ----> float
print("Hi %s, you are %d old" %(name, age))


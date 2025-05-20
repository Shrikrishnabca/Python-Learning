# Conditional statements decides execution flow based on specific condition
from Data_type.data_type_string import print_ch

# if statement executes if block condition is True
a = 10
if a > 5:
    print(f"{a} is greater than 5")  # 10 is greater than 5

# In line if statement
if a > 5: print(f"{a} is greater than 5")

# In line if statement
age = 18
if age >= 18: print("able to vote")

# if else if block of code executes condition was true, if not else block get executed
a= 20
if a < 10:
    print(f"{a} is less then 10")
else:
    print(f"{a} is greater than 10")
print(f"{a} is less than 10") if a < 10 else print(f"{a} is greater than 10")

# In line if-else
age = 23
print("able to vote") if age>= 19 else print("not able to vote")
age = 23
print("you can marry") if age >= 21 else print(" Sorry you cannot marry now")

# elif when ever we have a multiple condition to check we will use elif, if one block executes next condition will
# not check

age = 25
if age <= 10:
    print("child")
elif age <= 18:
    print("teenage")
elif age <= 25:
    print("young adult")
else:
    print("adult")

# nested if else: if else statement inside another if else statement




"""Python looping statements"""
# In python loops are used to execute same block of code multiple time
# Python provide 2 type of looping statements

# For loop Used to iterate over a sequence
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Range is built in function generate sequence of object
# Range have a arguments of start count, end count, step count
for i in range(5):
    print(i)

# While loop runs block of code as long as condition was true
i = 0
while i < 5:
    print(i)
    i += 1

# Loop control statement
# Break - break out of the loop
i = 10
while i < 100:
    print(i)
    if i == 50:
            break
    i += 10

# Continue used to skip the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# Else with loops: runs only when if loop wasn't break
for i in range(20):
    if i == 10:
        continue
else:
    print("Executing the else loop")
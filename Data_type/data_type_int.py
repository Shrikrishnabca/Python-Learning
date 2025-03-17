# Value store in a particular memory location or in variable is integer value its int data type.
a = 20
print(type(a))

# Anything you store as integer, it's object of builtin class int
# Default value of int is 0
# way to create an integer value either directly we can assign value or we can use built in function int()
a = int()
print(a)

# Type casting is a process of converting one data type into other
# float --> int
a = 10.012
print(int(a))

# bool --> int
a = True
b = False
print(int(a))  # 1
print(int(b))  # 0

# Write a python program to check number is even or not
number_to_check = int(input("Enter a number to check"))
if number_to_check % 2 == 0:
    print(f"{number_to_check} is a even number")
else:
    print(f"{number_to_check} is a odd number")
print(f"{number_to_check} is a {'even number' if number_to_check % 2 == 0 else 'odd number'}")

# Check the given number is a palindrome
if str(number_to_check) == str(number_to_check)[::-1]:
    print(f"{number_to_check} is a palindrome")
else:
    print(f"{number_to_check} is not a palindrome")

# Factorial of number 3!
fact_num = 1
for i in range(1, number_to_check + 1):
    fact_num *= i
print(fact_num)

# find the largest number in a list
a = [1, 3, 4, 6, 3, 5, 10, 2]
large = a[0]
for i in a:
    if i > large:
        large = i
print(large)

# Remove the duplicates from the
print(set(a))

res = []
for i in a:
    if i not in res:
        res.append(i)
print(res)

# Write a program to get positive value only
a = -20
print(abs(a))  # 20

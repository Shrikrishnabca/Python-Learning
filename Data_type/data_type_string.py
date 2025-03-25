# String is a collection off characters
# String is immutable - cannot change the original object
# String is bond with '', "", """"""
print('Helo world')
print("Hello world")
print("""Hello world""")

# len() is a built in function gives the length of collection data type
print(len("haii"))  # 4 counts starts from 1

# empty string
a = ''
b = str()
print(a, b)

# Raw string prefixed with r and its not consider the \ slash character its treat as a normal string
# in python \ character has special meaning
# \t tab
# \n new line
# \\ escape sequence
print("hello \n world")
print(r"Hello \n world")

# Indexing is a process of extracting one corrector at a time
# Indexing start from Zero
# In indexing we can give positive indexing or negative
a = "shrikrishna"

# First character
print(a[0])  # s
print(a[-len(a)])  # s

# last character
print(a[-1])  # a
print(a[len(a)-1])  # a

# slicing is process of extracting one or more character at a time
# str_obj[start index(0): end index(-1): step count(1)]
print(a[::])  # Whole string
print(a[::2])  # Even Index chatterers
print(a[1::2])  # Odd Index corrector
print(a[::3])  # dividend of 3 characters
print(a[::-1])  # reverse a string

# String formating is a process of injecting the dynamic value to the string during run time
# we will use {} and string prefixed with f""
name = "shri krishna"
name_1 = "shri krishna"
print(name_1 is name) # if create a string instance with same value it will not create new instance, instead
# both pointing to same instance in
print(f"my name is {name}")

# String builtin methods
# Upper() convert all character to upper case
print(name.upper())  # it will not modify original string, so its immutable
name = 'SHRI KRISHNA'

# lower() convert all character to lower
print(name.lower())

# dir() is built in function give all attributes attached to the object
print(dir(name))

# swap case() converts lower to upper and vice versa
print(name.swapcase())

# capitalize returns string starts with upper case
print(name.capitalize())

# count return number of occurrence of specified string in original string (case-sensitive)
name = "shri krishna"
# count(sub_string, start index, end index)
print(name.count("s"))  # 2
print(name.count("s", 1))  #  1

# returns zero if sub string is not present in original string
print(name.count("z"))


# merging string adding two string using arithmetic operator +
# is an example of operator overloading
print("Hello "+ "Krishna")

# Type conversion
# Number to string
a =123
print(str(a)) # "123"

# Floating to string
a =1.23
print(str(a))

# Boolean to string
a = True
print(str(a)) # "True"

# list to string
a = [1,2,3]
print(str(a)) # "[1,2,3]

# tuple to string
a = (1,2,3)
print(str(a)) # "(1,2,3)

# dictionary to string
print(str({'a': 1, 'b': 2}))  # "{'a': 1, 'b': 2}"

# None to string
print(str(None)) # "None"

# string to int
a = "12"
print(type(int(a)))

# string to list
a = "[1,2,3]"
print(list(a))  # it will treat each as a char ['[', '1', ',', '2', ',', '3', ']']
a = "123"
print(list(a))






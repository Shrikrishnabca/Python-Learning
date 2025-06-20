# file handling allow you to read,write and delete file from python program.

# Python provide built-in functions to handle file(open(), read(), write(), and close().)

# Modes in file handling
# "r" --> "Read the file(default)" ("error if not exist")
# "w" --> "Write the file(overwrite)" (" create if it not exists")
# "a" --> "Append the values to the file" (" create if it not exists")
# "x" --> "Create a file" ("error if it exist")


# opening a file
file = open("names.txt", "r")
file.close()

# reading from a file
file = open("names.txt", "r")

# Using read function
print(file.read())  # Give full content of the file
file.close()
# Once its read we can iterate agian

# Using for loop
# Each line has \n at the end
file = open("names.txt", "r")
for line in file:
    print(f"{line.strip()} from loop")
file.close()

# Read one line at a time
file = open("names.txt", "r")
print(file.readline())  # shrikrishna
file.close()

# Read all line into a list
file = open("names.txt", "r")
print(file.readlines())  # ['shrikrishna\n', 'nagraj\n', 'madhu\n', 'manu\n', 'raki']
file.close()

# file = open("names_1.txt", "r")  # raise a file not found error if it not present

# Writing to file
# if the file not presents create one
file = open("example.txt", "w")
file.write("Hello shri krishna")





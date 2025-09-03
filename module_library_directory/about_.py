# Module
# It is a simple python file ends with .py extension.
# that contains functions, classes, or variables you can use in other programs.

#  We have built in modules that are already available in python
import math
import datetime
import random

print(math.sqrt(16))        # 4.0
print(datetime.datetime.now())
print(random.randint(1, 10))


# Why Use Modules?
# Reuse code across multiple files
# Organize your code into logical parts
# Avoid writing the same code again
# Share your code with others easily

# Types of Modules
# Built-in Comes with Python
# User-defined	Modules you create
# Third-party	You install it
# Standard Lib	Part of the standard library (no install)

# library
# It is a collection of modules and packages, which provides ready to use functions, class and tools

# You want to generate a random number:
# Instead of writing your own logic, you just use Python’s built-in random library:

# Key Benefits of Libraries
# ✅ Save time
# ✅ Avoid rewriting code
# ✅ Use tested, reliable tools
# ✅ Focus on logic, not low-level tasks
# ✅ Build faster and better projects

# 🧠 Difference Between Library, Module, and Package
# Term	Meaning
# Module	A single .py file with Python code
# Package	A collection of modules in a folder with __init__.py
# Library	A broad term for tools/modules/packages grouped for a purpose

# Directory in Python
# its is a folder in our project
# It can contain files, like .txt, .py, .jpg, etc.
# It can also contain other directories, called subdirectories.

# Documents/
# ├── Projects/
# │   ├── app.py
# │   └── data.csv
# ├── Resume.docx
# └── Notes.txt

# Documents is a directory.
# Projects is a subdirectory.
# app.py, data.csv are files inside a directory.

# Package is a special directory which contains python modules
# It allows you to organize related code in a structured and reusable way
# A package = folder with an __init__.py file and modules inside it.

# Why Use Packages?
# Organize code logically (e.g., math, data, utils)
# Avoid name conflicts
# Reuse code easily
# Create scalable projects


# my_package/              <- ✅ package
# ├── __init__.py          <- makes it a package
# ├── add.py               <- module
# ├── subtract.py          <- module

# 🧩 Difference Between Package and Directory in Python
# Feature	Directory	Package (in Python)
# 🔹 Basic Meaning	A folder on your file system	A special directory used to structure Python code
# 🔹 Contains	Any files (images, docs, code, etc.)	Python modules (.py files) and __init__.py file
# 🔹 Purpose	For storing files	For organizing Python code into namespaces
# 🔹 Special File	❌ No need for any special file	✅ Must contain __init__.py (in Python < 3.3 or to mark it explicitly)
# 🔹 Used In Code	Not directly	✅ You can import modules from it
# 🔹 Recognized by Python	❌ No	✅ Yes, if it has __init__.py

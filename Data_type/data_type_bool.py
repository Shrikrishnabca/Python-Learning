# Value stored in particular memory location is True or False its belongs to bool data type
a = True
print(type(a))

# Dfault value of bool if False
a = bool()
print(a)

# Type casting
print(int(True))  # 1
print(int(False))  # 0
print(float(True))  # 1.0
print(float(False))  # 0.0

# Boolean is a subtype of int
print(isinstance(True, bool))  # True
print(isinstance(False, bool))  # True
print(isinstance(True, int))  # True

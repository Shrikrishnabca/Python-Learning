 # Collection of kye and value pair
# Each pair has unique keys
# Key must be immutable or hashable
# Value can be duplicate
# Dictionary is mutable

# Dictionary creation
a = dict()
print(a)  # {}

c = dict(apple= 1, mango=20)
print(c)

b = {"apple": 1, "mango": 2}
print(b)

# Dictionary can have tuple as key
a = {(1,2): "number", (1.0, 2.0): "floating"}

# Accessing the value of dictionaries
a = {"apple": 1, "mango": 2}
print(a.get("apple"))  #  Returns the value for specified key

print(a["apple"])  # Kind of indexing using key

# Adding/ updating the dictionary
a["banana"] = 5
print(a)  # {'apple': 1, 'mango': 2, 'banana': 5}

# Updating the existing the dictionary with specified item
a.update({"grapes": 3, "jackfruit": 1})
print(a)  # {'apple': 1, 'mango': 2, 'banana': 5, 'grapes': 3, 'jackfruit': 1}
a.update(moosambi=2)
print(a)  # {'apple': 1, 'mango': 2, 'banana': 5, 'grapes': 3, 'jackfruit': 1, 'moosambi': 2}

a.setdefault("orange")  # For the kye set default value None, if it is not given
print(a)  # {'apple': 1, 'mango': 2, 'banana': 5, 'grapes': 3, 'jackfruit': 1, 'moosambi': 2, 'orange': None}

# Create dictionary with specified itable and value
print(a.fromkeys([1,2], [11]))

# total item in a dictionary
print(len(a))  # 7

# Deleting the key and value
# pop() remove the specified item from the dictionary, return the value of removed element
# Raise key error if specified kye not present
print(a.pop("orange"))

# popitem() remove the last added item return in the tuple formate
print(a)
print(a.popitem())  # ('moosambi', 2)

# Merging the dictionary
a = {"apple": 1, "mango": 2}
b = {"naga": 1, "madhu": 2}
c = { **a, **b}
print(c)










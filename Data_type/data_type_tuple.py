# Tuple is a collection of homogeneous and heterogeneous elements
# Tuples are immutable
# Tuple are ordered, allow duplicate elements
# We can do slicing and indexing

# Tuple creation
a = tuple()
print(tuple((1,2,3)))
print(a)  # Create empty tuple
a = (1,)
print(a)  # Creating tuple with one object

a = (1,2,3,4,8,6,5,4)

# len() give the item in a list
print(len(a))  # 8

# Slicing
print(a[0])  # 1
print(a[-1])  # 5
print(a[::-1])  # reverse order (5, 6, 8, 4, 3, 2, 1)

# built-in methods
# count() will give the count of specified object
print(a.count(4))  # 2

# index() give the index of specified object
print(a.index(4))

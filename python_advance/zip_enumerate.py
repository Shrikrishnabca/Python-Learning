# The zip() function combines two or more iterables (like lists or tuples) element by element into tuples.
names = ['Krishan', 'Ravi', 'Pooja']
scores = [90, 85, 92]

combined = zip(names, scores)
print(list(combined)) # [('Krishan', 90), ('Ravi', 85), ('Pooja', 92)]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

a = [1, 2, 3]
b = ['a', 'b']

print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]

pairs = [('Krishan', 90), ('Ravi', 85)]
names, scores = zip(*pairs)

print(names)   # ('Krishan', 'Ravi')
print(scores)  # (90, 85)

names = ['a', 'b', 'c']
scores = [1, 2, 3]

d = dict(zip(names, scores))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# enumerate() is a built-in Python function that adds a counter (index) to an iterable and
# returns it as an enumerate object (which you can loop over).

for index, value in enumerate(names):
    print(index, value)

fruits = ['apple', 'banana', 'mango']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")


# 1. apple
# 2. banana
# 3. mango

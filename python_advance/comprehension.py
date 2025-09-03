# Comprehension is a concise way to construct sequences (like lists, sets, dicts)
# using a single line of code.

# List Comprehension

a = [i for i in range(20) if i % 2 ==0]
print(a)
b = [i*i for i in range(20)]
print(b)
c =[i if i % 2 == 0 else i* 0 for i in range(20)]

# set
a = {i for i in range(20) if i % 2 ==0}
print(a)
b = {i*i for i in range(20)}
print(b)
c ={i if i % 2 == 0 else i* 0 for i in range(20)}

# Dictionary
a = {i:i for i in range(20) if i % 2 ==0}
print(a)
b = {i:i*i for i in range(20)}
print(b)
c ={i: i if i % 2 == 0 else 0 for i in range(20)}




# Using for condition checking
checking = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(checking(1))
print(checking(-1))
print(checking(0))

# using with list comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())


# using to return multiple result
calc = lambda x, y: (x + y, x * y)
print(calc(2, 5))

# using in filter function
numbers = [1, 2, 3, 4, 5, 6, 7]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

# using with map
converted = map(lambda x: x * 2, numbers)
print(list(converted))

# using with reduce
from functools import reduce
reduced = reduce(lambda x, y: x * y, numbers)
print(reduced)
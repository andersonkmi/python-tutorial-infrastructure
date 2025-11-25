from functools import reduce
import operator

li = ['Software', 'engineering', 'course']
res = reduce(lambda x, y: x + " " + y, li)
print(res)

# Using named function
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)

# Using operator
a = [2, 4, 2, 6, 8]
print(reduce(operator.add, a))
print(reduce(operator.mul, a))
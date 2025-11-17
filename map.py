# simple example
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

# convert a map to a list
def double(val):
    return val * 2

a = [1, 2, 3, 4]
res = list(map(double, a))
print(res)

# map with multiple iterables
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]

res = map(lambda x, y: x + y, a, b)
print(list(res))

# converting strings to all uppercase
fruits = ['apple', 'banana', 'mango']
res = map(str.upper, fruits)
print(list(res))
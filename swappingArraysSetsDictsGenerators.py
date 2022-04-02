x = 10
y = 11

x, y = y, x
#this is swapping

"""ARRAYS"""

from array import array

numbers = array("i", [1,2,3])
numbers[0] = 2
#operations on lists work here too

"""SETS"""
number = [1,1,2,3,4]
first = set(numbers)
second = {1,5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
if 1 in first:
    print("yes")
"""DICTIONARIES"""
point = {"x":1, "y":2}
point = dict(x=1, y=2)
print(point["x"])

if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)

#/////////////////////////////

values = []
for x in range(5):
    values.append(x*2)
values = [x*2 for x in range(5)] #this does what the 3 above lines do
values = {x: x * 2 for x in range(5)}
"""GENERATORS"""

values = [x * 2 for x in range(10)] #gives generator object on it's own
for x in values:
    print(x)

#generators are far more efficient than lists if we can use them

"""UNPACKING OPERATOR"""

values = list(range(5))
[*range(5)]
print(values)
# * symbol is unpacking operator
# ** combines 
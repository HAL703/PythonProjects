items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30),
]

def sort_item(item):
    return item[1]
"""The two lines above become obsolete with the following lambda function"""

items.sort(key=lambda item:item[1])
print(items)

"""MAP FUNCTIONS - TO TRANSFORM INTO A LIST OF NUMBERS AND PRICES"""

prices = []
for item in items:
    prices.append(item[1])

print(prices)

"""MAPPED ORIGINAL LIST INTO NEW LIST"""

"""BUT... A MORE ELEGANT WAY"""

x = map(lambda item: item[1], items)
for item in x:
    print(prices)

"""HOWEVER..."""

prices = list(map(lambda item: item[1], items))
print(prices)


"""FILTER FUNCTION WITH LAMBDA"""

"""ONLY GET ITEMS WITH PRICE GREATER THAN OR EQUAL TO 12 DOLLARS"""

x = filter(lambda item: item[1] >= 10, items)
print(x)
"""this gives filter object, so let's convert to list"""
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

"""LIST COMPREHENSIONS DO WHAT MAPPING AND FILTERING DOES"""
"""------------------------------------------------------------------"""
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] 
"""for each item, does same thing as map"""

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
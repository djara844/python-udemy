# Set tuple
fruits = ('orange', 'banana', 'guava')

# Len tuple
print(len(fruits))

# Show element for index
print(fruits[1])
print(fruits[-2])

# Show elements for range
print(fruits[0:1]) # Is exclusive

# Iterate tuple
for fruit in fruits:
    print(fruit, end=' ')

# Update value
# Convert tuple to list, update values and convert listo to tuple
fruitsList = list(fruits)
fruitsList[0] = 'Apple'
fruits = tuple(fruitsList)
print('\n', fruits)

# Delete tuple
del fruits

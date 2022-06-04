names = ['Juan', 'Karla', 'Ricardo', 'María', 0, 10, True, False]

# Print list
print(names)

# Show element
print(names[2])
print(names[-2])

# Show elements in range
print(names[0:2])# index 2 exclusive

print(names[: 3])# star to end - 1

print(names[1:])# index star to end

# Update value
names[3] = 'Diego'

# Iterate list
for name in names:
    print(name)

# Len list
print(len(names))

# Add element
names.append('Gina')

# Add element in index
names.insert(1, 'Isabel')

# Remove element for value
names.remove('Diego')

# Remove lastest value
names.pop()

# Remove for index
del names[0]
print(names)

# Clear list
names.clear()

# Delete list in memory
del names

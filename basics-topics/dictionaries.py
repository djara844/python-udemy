# Define dictionary, key => value
elements = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

# Len dictionary
print(len(elements))

# Show value for key
print(elements['IDE'])
print(elements.get('IDE'))

# Update value
elements['IDE'] = 'integrated development environment'

# Iterate dictionaries
for key, value in elements.items():
    print(key, value)

# Show values
for value in elements.values():
    print(value)

# Show keys
for key in elements.keys():
    print(key)

# Validate key exist
print('IDE' in elements)

# Add element
elements['PK'] = 'Primary key'

# Remove element for key
elements.pop('DBMS')

# Clear dictionay
elements.clear()

# Delete dictionay in memory
del elements

print(elements)
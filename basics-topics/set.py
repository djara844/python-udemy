# Define set
# Not order, nor duplicate elements

planets = {'Mars', 'Jupiter', 'Venus'}
print(planets)

# Len set
print(len(planets))

# Find element
print('Mars' in planets)

# Add element
planets.add('Earth')

# Remove elements
# Is possible show error
planets.remove('Earth')
# Not show error
planets.discard('Jupiter')
# Clear set
planets.clear()
# Delete set
del planets

print(planets)


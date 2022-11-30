# A dictionary is a collection which is unordered, changeable and indexed. No duplicate member

# Create dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person)

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key and value
person['phone'] = '5555-5555-555'

# Get dic keys
print("ini keys ", person.keys())

# get dic items
print("ini items ", person.items())

#copy dict 
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# list of dict

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Ambar', 'age': 25},   
]

print(people)
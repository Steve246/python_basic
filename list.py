# list kayak array

# create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oraanges']

# use a constructor

number2 = list((1,2,3,4,5))

print(numbers)
print(number2)

# Get Value
print(fruits[1])

# Get Length
print(len(fruits))

#Append to list
print(fruits)
fruits.append("Manggos")
print(fruits)

# remove from list
fruits.remove('Manggos')
print(fruits)

# insert into spesific position
fruits.insert(1, 'Strawberies')
print(fruits)

# Change value in list
fruits[0] = 'Blueberies'
print(fruits)

# remove with pop
fruits.pop(2)
print(fruits)

#reverse list
fruits.reverse()
print(fruits)




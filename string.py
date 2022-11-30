# strings in python used single or double quote

iniApa = "huello"

hello = 'hallo'


print(iniApa, hello)

# concatenate --> combine string 

stringFirst = "this is first"
stringSecond = "this is second"

age = 35
name = "Stevem"

combineString = stringFirst + " " + stringSecond + " " + str(age)

print(combineString)

# Argument by position

print( 'My name is {name} and I am {age}'.format(name=name, age=age))

# F string --> only for python (3.6+)

print(f'Hello, my name is {name} and i am {age}')

# String methods

s = "hello world"

# Capitalize String

print(s.capitalize())

# Make all upercase

print(s.upper())

# Make all lower

print(s.lower())

# Swap Case

print(s.swapcase())

# Get Length

print(len(s))

# replace

print(s.replace('world', 'everyone'))

# count --> count world h inside string s

sub = 'h'
print(s.count(sub))

# Starts with

print(s.startswith('hello'))

# end with

print(s.endswith('d'))

# split into list

print(s.split())

# find position of alphabet

print(s.find('r'))
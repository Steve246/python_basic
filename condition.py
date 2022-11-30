x = 5
y = 21


# Simple if

if x > y:
    print(f'{x} is greater than {y}')
    
# elif

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else: 
    print(f'{y} is greater than {x}')

# Nested if 

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or , not) - Used to combine conditional statement

if x > 2 and x <= 10:
    print(f'{x} is greater thann 2 and less than or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is greather than 2 or less than or equal to 10')


if not (x == y):
    print(f'{x} is not equal to {y}')

# membership operators (not, not in) - Membershop operators are used to test if a sequence is presented in an object

number = [1,2,3,4,5]

# in 
if x in number: 
    print(x in number)
    
# not in 
if x not in number:
    print(x not in number)
    
# identify operators (is, is not) - compare the object, not if they are equal, but id they are actually the same object, with the same memory location

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)
    
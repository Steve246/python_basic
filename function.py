
# Create function

def sayHello(name):
    print(f'Hello{name}')

sayHello('John Doe')


# Return value

def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3,4)
print(num)

# lamda function, is a small anonyomous function
# can take any number of arguments, but can only have one experession. Very similar to JS arrow function

getSum = lambda num1, num2: num1 + num2

print(getSum(11,3))

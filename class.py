# class, an object has properties and methods (function) associated with it. Almost eveything in Python is an object


# Create Class
class User:
    #Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1
    
    def set_balance(self, balance):
        self.balance = balance


# Extends Class
class Customer(User):
    # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance
        
    
    def greeting(self):
        return super().greeting() + f' and my balance is {self.balance}'


# init user object
brad = User('Brad Traversy', 20, "tedj@gmail.com")
# print(brad.name, type(brad), type(brad.name))
# print(brad.age, type(brad.age) , brad.email)

brad.has_birthday()
print(brad.greeting())

janet = Customer("Janet Williams", 25, "janet@gmail.com")

janet.set_balance(500)

print(janet.greeting())





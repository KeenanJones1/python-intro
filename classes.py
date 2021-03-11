#  A class is like a blueprint for creating objects. An object has properties and methods  (functions) associated with it. Almost everything in Python is an object.

# create a class

class User:
    # constructor - a fucntion that runs when you create a instance of the class.
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extends class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# init user object
keenan = User('Keenan Jones', 'afew@gmail.com', 27)
# print(type(keenan))
# output <class '__main__.User'>

# print(keenan.name)
# Keenan Jones
keenan.has_birthday()
# print(keenan.greeting())


cash = Customer('James', 'jasme12@gmail.com', 45)
cash.set_balance(50000000)
# print(type(cash))
# print(cash.balance)
cash.has_birthday()
print(cash.greeting())

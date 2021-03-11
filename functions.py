# def keyword starts a function
def greeting():
    print('Hello there my friend')
    print('What is your name ?')
    name = input()
    print(" Nice to meet you " + name)


# Invocation of a function
# greeting()

# parameters
def parameter_func(name):
    print('Hello there ' + name)


parameter_func('Keenan')


# return function
def multiply_by_10(number):
    return 10 * number


multiplied_number = multiply_by_10(4)
# print(multiplied_number)

# default parameter


def add(number, by=1):
    return number + by


# added_number = add(10, 5)
added_number = add(10)
# print(added_number)

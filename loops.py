# For loop
users = ['Ed', 'Ana', 'John', 'Podrick']

# for user in users:
#     print(f'Hello there {user}')

# list keyword creates a list of whatever is passed in
# name = list('Edwin')
# print(name)

# pass in a starting value and a end value.
# range(starting, ending, incremenation)
my_list = list(range(0, 101, 10))
# print(my_list)


# for i in range(0, 5):
#     print('I run 5 times')

# looping over string
name = 'Keenan'
# for letter in name:
#     print(letter)


# While loop runs intl the statement is false
# break = breaks the loop
# continue skips over something

age = 10
while(age < 20):
    age += 1
    if(age == 14):
        continue
    print(age)

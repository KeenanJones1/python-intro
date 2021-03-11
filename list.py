# Used to hold multiple values

users = ['Ed', 'Homeboi', 'Ana', 'Ronny', 'Pepper']
# print(users[0])


alot_zero = [0] * 20
# print(alot_zero)


# slicing arrays
# print(users[0:3])


# unpacking
items = ['Laptop', 'Phone', 'Joystick']
laptop, *other = items
# print(laptop)


# builting methods

# Add items to end of list
users.append('Oranges')
# print(users)

# Add to specifc place
users.insert(1, 'Bacon')
# print(users)

# remove items
users.pop()
# print(users)

# end of built in methods

# Tupples can only be read and iterate
letters = ('a', 'b', 'c', 'd')


# Sets only can have unqiue items
set_letters = {'a', 'b', 'c', 'd'}

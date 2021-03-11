#
fruit = 'Apple'
other_fruit = fruit
other_fruit = 'Oranges'
# print(other_fruit)


fruits = ['Apple', 'Orange', 'Dragon', 'Pears']

other_fruits = fruits

# This changes fruits as well as other_fruits
other_fruits.append('Berry')

# print(fruits)


# To successfully copy a list do the following.

other_fruits = fruits.copy()

other_fruits.append('Kiwi')
print(fruits)
print(other_fruits)

# mutables = can change but not mess up the og one: bool, ints, floats, tuples,strings

# immutable = changing a copy w/o using the copy method will change the og: lists, sets, dicts, Always keep a reference.

# Key pair Values

import random
user = {"name": 'Keenan', "email": 'Kudon@gmail.com',
        "age": 34, "purchases": [1, 2, 3, 4, 5]}

# print(user["name"])

# Changing dict values
user["name"] = 'Paul'
# print(user["name"])

# iterate through dict
# for key in user:
#     print(key)

# methods
# print(user.keys())
user.keys()

# both keys and values
# items = items in dict
# for key, val in user.items():
#     print(key)
#     print(val)

# if "name" in user:
#     print('it is !')

if "logged" in user:
    print("It is !")


guess_number = random.randint(0, 20)
print(guess_number)

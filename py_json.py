# JSON, commonly used with data apis. Here how we can parse JSON into a python dictionary.
import json
# naming the file json.py would cause a conflict when importing this module.

# Sample JSon
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJSON)
# print(user)
# print(user['first_name'])

# dict to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)

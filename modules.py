#  A module is a file containing a set of fuctions to include in your application.

# There are core python modules/modules you can install using the pip package manager (including Django) as well as custom modules.

# pip is similar to ruby gems or npm packages. pip install
# for python3 used pip3

# importing is a way to use core python modules w/o pip installing

# import time
from time import time

# import datetime
from datetime import date

# pip module
from camelcase import CamelCase

# import custom module
# go to validator to check out how to import custom modules.
import validators
from validators import validate_email

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('email is bad')


# today = datetime.date.today()
today = date.today()
# print(today)

# timestamp = time.time()
timestamp = time()
# print(timestamp)

c = CamelCase()
# print(c.hump('hello there world'))
# outputs Hello There World

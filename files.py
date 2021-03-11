# Python has functions for creating, reading, updating and deleting files.

#  open a file
# also creates a file.
myFile = open('myFile.txt', 'w')

# get file info
print('Name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# write to file
myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to File
myFile = open('myFile.txt', 'a')
myFile.write('I also Like Ruby on Rails')
myFile.close()

# Read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)

language = 'Python'

# string functions

# check how many chars are in a string
letter_count = len(language)
# print(letter_count)


# Access chars
letter = language[4]
# print(letter)

# Access chars from to
consec_letters = language[0:3]
# print(consec_letters)


# back to beginning of stirng
start_letter = language[-6]
# print(start_letter)

# string methods
upper_language = language.upper()
# print(upper_language)


new_string = "The Mother of the Dragons WAS WILD"

lower_string = new_string.lower()
# print(lower_string)

# find index
find_please = new_string.find('the')
# print(find_please)

# replace old text with new text

replace_string = new_string.replace('Mother', 'Joffrey')
print(replace_string)

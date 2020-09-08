"""
Program: string_method.py
Author: Grayson Hardin
Last date modified:


This file provides a list of various methods and briefly explains their purpose.
"""


# Variable
movie_character = 'Keanu Reeves in John Wick.'

# Capitalized method: This will capitalize the first character of a string and lower any additional upper cases that occur after.
print(movie_character.capitalize())

# Find method: This will find the given value and show which character placement it is stored in (i.e: If the value was 'K' it would return 0.)
print(movie_character.find('John'))

# Index method: This will show the placement value (similar to the previous method) but it is mainly used for sub-strings.
print(movie_character.index('John Wick'))


# Isalnum method: Since there are spaces and no integers in the movie_character variable, the result is False.
print(movie_character.isalnum())


# Isalpha method: Similar to the previous, the isalpha method will return 'True' if all the characters in the string are in the alphabet, no spaces, and can be lower/upper case. If there is a space, it will return 'False'
print(movie_character.isalpha())


# Isdigit method: If the string contains all numbers, then it will return 'True.' Likewise, it will return 'False' if there is none.
print(movie_character.isdigit())


# Islower method: The Islower method will return 'True' if the string is all lowercase and it will return 'False' if at least one character is uppercase.
print(movie_character.islower())


# Isupper method: If all of the characters are uppercase, it will return 'True.' Again, it will return 'False' if at least one is lowercase.
print(movie_character.isupper())


# Isspace method: At first glance, one might think this checks for spaces, but it actually checks for whitespaces (i.e: '  \t').If it contains a whitespace, the result is 'True' and 'False if there is none.
print(movie_character.isspace())


# Startswith method: This method checks whether the variable starts with a given value. In our case, our first character in the string 'movie_character" starts with 'K' and thus, the return value is True.
print(movie_character.startswith('K'))


"""
Program: listOne.py
Author: Grayson Hardin
Last date modified: 9/10/2020


This file provides different ways to use the list methods and briefly explains their purpose.
"""

# This is my variable with an assigned list.
my_list = ['best', 'job', 'ever']
print(my_list)

# Append method: This will add an additional value to the already existing list.
my_list.append('am I right?')
print(my_list)

# Clear method: As its name suggests it will clear the list of its values. Be sure to block this out otherwise it will make the following methods fail since it clears the list.
# my_list.clear()
# print('Cleared lists:', my_list)


# Copy method: This will copy a list.
new_list = my_list.copy()
print("Copied list:", new_list)

# Count method: This will literally count how many times the given value is declared within a list.
count = my_list.count('best')
print(count)

# Extend method: The following method will take the current list and add values to it.
my_list_extend = ['do you agree?']
my_list.extend(my_list_extend)
print('The extended list is:', my_list)

# Index method: This method will show which placement the value is in (i.e: the word "best" is in placement 0 while 'ever' is on the second placement.)
index = my_list.index('best')
print('The index of ever is:', index)

# Insert method: The insert command will replace the value stored in "0" with a new value.
my_list.insert(0, 'new')
print('New inserted list:', my_list)

# Remove method: This will remove any given value from the list.
my_list.remove('ever')
print('Removed an item from list:', my_list)

# Reverse method: This will reverse the list from right to left.
my_list.reverse()
print(my_list)

# Sort method: This command will sort the list from alphabetical order.
my_list.sort()
print(my_list)

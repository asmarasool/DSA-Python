# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type,
# but the keys must be of an immutable data type such as strings, numbers, or tuples.
dict = {'Name': 'Nila', 'Age': 34, 'Class': 'Online'}


# Accessing Values in Dictionary
print(dict["Name"]) # access by key not value
# print(dict[34]) ## error

# Updating Dictionary
dict['gender'] = 'F' # add new entry
print(dict)
dict['Age'] = 34.5 # update existing
print(dict)

# Delete Dictionary Elements
del dict['gender'] # Deletes entry with key gender
dict.clear()       # removes all entries of the dict
del dict           # Deletes entire dictionary

# ** Important
# no duplicate key is allowed
# Keys must be immutable( strings, numbers or tuples),
# a list like ['key'] cannot be key
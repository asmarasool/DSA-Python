# manage multiple dictionaries together as one unit.
# eliminating any duplicate keys
# The best use of ChainMap is to search through
# multiple dictionaries at a time and get the proper key-value pair

import collections

# creating a map
dict1 = {"name": "Maryam", "Age": 26, "gender": "F"}
dict2 = {"name": "Nila", "Class": "Python", "Score": 100}

mapping_result = collections.ChainMap(dict2, dict1)
print(mapping_result.maps, '\n')

for key, value in mapping_result.items():
    print(key, value)

print(list(mapping_result.keys()))

# Map reordering
mapping_result = collections.ChainMap(dict1, dict2)
print(mapping_result.maps) # dict1 displays first

# updating a map
dict1["name"] = "Asma"
print(mapping_result.maps) # Nila is updated to Asma

dict1["Employer"]= "VSJL"
print(mapping_result.maps)


## creat array
from array import *
## arrayName = array(typecode, [Initializers])
# Typecodes
# b	Represents signed integer of size 1 byte
# B	Represents unsigned integer of size 1 byte
# c	Represents character of size 1 byte
# i	Represents signed integer of size 2 bytes
# I	Represents unsigned integer of size 2 bytes
# f	Represents floating point of size 4 bytes
# d	Represents floating point of size 8 bytes

array1 = array('i', [10, 20, 30, 40, 50])

for x in array1:
    print(x)

## Accessing Array Element
print(array1[2])

## Insertion Operation
array1.insert(4,100) # insert 100 at index 4
print(array1)

# Delet from an array
array1.remove(array1[0])
array1.remove(30)
print(array1)

# Search in an array
print(array1.index(20))

# Update an array
array1[2] = 250
print(array1)
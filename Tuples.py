# A tuple is a sequence of immutable Python objects

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d", "e")

# Accessing Values in Tuples
print(tup1[2])
print(tup3[2:5]) # start at 2 goes to 5 but not including 5


# Updating tuples
# Tuples are immutable which means you cannot update or
# change the values of tuple elements.
# combine tuples
tup5 = tup2 + tup1
print(tup5)

# Deleting tuples
del tup3
# print(tup3)

# Basic Tuples Operations
print(len(tup2)) # lenght
tup_combine = tup1 + tup2 # Concatenation
print(tup_combine)

# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
# 3 in (1, 2, 3)	True	Membership
# for x in (1, 2, 3): print x,	1 2 3	Iteration

# Unpacking tuples
x, y, z = "Nila", "Huma", "Miran"
print(x)
print(y)
print(z)

for t in enumerate("abcd"):
    index, char = t # t prints index and char in a tuple so we can unpack it
    print(index, char)
# set is a collection of items not in any particular order
# The elements in the set cannot be duplicates.
# The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
# There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

days_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_set = set(days_list)

days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}

# Accessing values in a set
# No indexing is supported
for i in days_set:
    print(i)

# Adding item to a set
days_set.add("golshanbe")
print("Adding golshanbe:", days_set)

# Removing from a set
days_set.discard("Mon")
print("Mon is deleted", days_set)

# unions of sets |
# combines two sets and removes duplicates like 10
num1 = {1, 3, 5, 7, 9,10}
num2= {2, 4, 6, 8, 10}
nums_union = num1 | num2
print("Union of nums", nums_union)

# Intersection of Sets &
num1 = {1, 3, 5, 7, 9,10}
num2= {2, 4, 6, 8, 10}
nums_intersect = num1 & num2
print("intersection of nums: ", nums_intersect)

# Difference of Sets
num1 = {1, 3, 5, 7, 9,10}
num2= {2, 4, 6, 8, 9 , 10, 1200}
nums_difference = num1 - num2
print("set difference: ", nums_difference)
nums_difference2 = num2 - num1
print("set difference 2: ", nums_difference2)

# compare sets (subsets and supersets)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

subset = DaysA <= DaysB # Subset
print(subset)
superset = DaysA >= DaysB # superset
print(superset)



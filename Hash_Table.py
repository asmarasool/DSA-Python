student = {"name": "Nila",
           "class": "python",
           "score": 100}

print(student["name"])
print(student["score"])
student["score"] = 99
print(student["score"])
# adding new entry
student["Age"] = 34
print(student)
del student["Age"]
print(student)
student.clear()  # deletes all the items in a list and leaves the dic empty
print(student)
del student  # delete the dic entirely
print(student)
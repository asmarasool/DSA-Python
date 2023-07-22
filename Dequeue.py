# A double-ended queue, or deque,
# supports adding and removing elements from either end

import collections

myList = ["Shabana", "Irfan", "Arman", "Nila"]
myDequeue = collections.deque(myList)

myDequeue.append("Maro") # Adds Maro to the right
print(myDequeue)

myDequeue.appendleft("Huma") # appendleft adds items at the beginning/ left
print(myDequeue)

myDequeue.pop() # deletes from right
print(myDequeue)

myDequeue.popleft() # deletes form the left 
print(myDequeue)
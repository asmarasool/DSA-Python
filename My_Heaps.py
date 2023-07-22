# Min Heap: Parent node SMALlER or EQUAL child note
# Max Heap: Prent node GRATER or EQUAL to child note

# Creating a heap
# A heap is created by using python’s inbuilt library named heapq.
import heapq

mylist = [6, 2, 10, 4, 5, 0]
# heapify >> This function converts a regular list to a heap.
# In the resulting heap the smallest element gets pushed to the index position 0
heapq.heapify(mylist)
print(mylist)

# Inserting into heap
heapq.heappush(mylist, 1000) # heappush adds at the last index
print(mylist, "heappush")

# Removing from heap
heapq.heappop(mylist) # heappop deletes the smallest element in a heap
print(mylist, "heappop")

# Replacing in a Heap
heapq.heapreplace(mylist, 999) # replaces the smallest element and insert with no order
print(mylist)


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
    # my_sorted = []
    # for i in range(len(h)):
    #     my_sorted.append(heapq.heappop(h))
    # return my_sorted

# heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
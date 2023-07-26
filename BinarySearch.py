def binarySearch_iterative(lst, target):
    """
    Iterative solution for a binary search function that takes only two arg.
    :param lst: a list for the function to search the target
    :param target: interger for the function to find in the list
    :return: the index of the target or -1 if the target does not exist in the list
    """
    first, last = 0, (len(lst) - 1)
    while first <= last:
        mid = (first + last) // 2
        if target == lst[mid]:
            return mid
        if target < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1


mylist = [1,2,4,8,10,18,100]
# print(binarySearch_iterative(mylist, 100))

##################################################

def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid if arr[mid] == target else None
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search((arr[mid:]), target)
            return mid + callback_response if callback_response is not None else None
        else:
            return recursive_binary_search((arr[:mid]), target)


mylist = [1,2,4,8,10,18,100]
print(recursive_binary_search(mylist, 10))

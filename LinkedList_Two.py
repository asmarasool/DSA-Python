class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# node1 = Node("Nila", "asma")
# print(node1.data)
# print(node1.next)
# node1 = Node("Huma")
# node2 = Node("Nila")
# node3 = Node("Shabana")
# node4 = Node("Maryam")
#
# node1.next = node2  #
# node2.next = node3  #
# node3.next = node4  #
#
# current_node = node1
# while True:
#     print(current_node.data)
#     if current_node.next is None:
#         print("None")
#         break
#     current_node = current_node.next

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, item):
        node = Node(item)  # create a node using Node class with "data" value
        if self.head is None:  # checking if the linked list is empty
            self.head = node  # the node we just created becomes the head
            return  # done with adding the first item to the list
        current_node = self.head  # if the linked list is not empty then we start
        # form head of the list and iterated through
        # the list until we find the last itme in the list
        # create a variable to store the current node, and we assign it to head
        while True:  #
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def print_LinkedList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node)


ll = linkedList()
ll.append("Huma")
ll.append("Nila")
ll.append("Shabana")
ll.print_LinkedList()

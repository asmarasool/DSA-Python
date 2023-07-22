# Doubly Linked List contains a link element called first and last.
# Each link carries a data field(s) and two link fields called next and prev.
# Each link is linked with its next link using its next link.
# Each link is linked with its previous link using its previous link.
# The last link carries a link as null to mark the end of the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



class doubly_linkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):  # Adding data to the beginning of the list
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, new_data): # adding data to the end of the list
        new_node = Node(new_data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = new_node
        return

    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next


doubly_ll = doubly_linkedList()
doubly_ll.push("Nila")
doubly_ll.push("Huma")
doubly_ll.push("Maro")
doubly_ll.push("Shab")
doubly_ll.append("Miranak")
doubly_ll.listprint(doubly_ll.head)

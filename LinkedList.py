# free code camp

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        node = Node(new_node)
        current_node = self.head
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

    def delete(self, weak_node):
        current_node = self.head
        if current_node.data == weak_node:
            self.head = current_node.next
        else:
            while current_node:
                if current_node.data == weak_node:
                    break
                prev = current_node
                current_node = current_node.next
            prev.next = current_node.next
            if current_node == None:
                return print('LInked list is empty')
            # current_node = None

    def insert(self, new_node_value, position):
        new_node = Node(new_node_value)
        count = 1
        current_node = self.head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        while current_node:
            if count+1 == position:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            else:
                count += 1
                current_node = current_node.next
        # pass

    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



ll = linkedList()
ll.append("Huma")
ll.append("Nila")
ll.append("Shabana")
ll.append("Maryam")
ll.print_ll()

ll.delete("Maryam")
ll.print_ll()

ll.insert("abc", 1)
ll.print_ll()
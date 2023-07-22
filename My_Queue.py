# First-in-First out
# .pop always deletes the last element in a list

# queue = ["a", "b"]
# queue.insert(0, "Nila")
# print(queue)
# queue.pop()
# print(queue)

class queue:
    def __init__(self):
        self.q = list()

    def add(self, data):
        if data not in self.q:
            self.q.insert(0, data)
            return True
        return "Data is already in the list."

    def delete_form_q(self):
        if len(self.q) > 0:
            return self.q.pop()
        return "No data in the list."

    def print_queue(self):
        for i in self.q:
            print(i)

myQueue = queue()
myQueue.add("Nila Jan")
myQueue.add("Miran")
myQueue.add("Maryam")
# myQueue.print_queue()
myQueue.delete_form_q()
myQueue.print_queue()

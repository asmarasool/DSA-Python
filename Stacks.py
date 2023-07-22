# Last in First Out(LIFO)
# The operations of adding and removing the elements is known as PUSH and POP
class stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            print("stack is empty!")
        else:
            self.stack.pop()

    def last_item(self):
        return self.stack[-1]

my_stack = stack()
my_stack.push("Nila")
my_stack.push("Maryam")
my_stack.last_item()
print(my_stack.last_item())
my_stack.pop()
print(my_stack.last_item())
my_stack.pop()
my_stack.pop()
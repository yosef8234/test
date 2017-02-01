class Stack:
    def __init__(self):
        self.items = []
        self.max = 5
    def push(self, item):
        if len(self.items) < 5:
            self.items.append(item)
        else:
            print("abort push in order to prevent stack overflow")
    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print("stack is empty, abort pop to prevent stack underflow")
    def print_stack(self):
        print(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6) # abort push in order to prevent stack overflow
stack.pop()
stack.print_stack() # [1, 2, 3, 4]
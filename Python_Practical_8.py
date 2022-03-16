## Archana Vyas
## 20CE157
## Git Repository: https://github.com/Archna1304/Python_Practical-8.git

# Stack implementation in python

# Creating a stack
class Stack:
    def __init__(self):
        self.items = []
        
## Define methods push, pop and is_empty inside the class Stack.

#The method is_empty returns True only if items is empty
# Creating an empty stack
    def is_empty(self):
        return self.items == []
    
# The method push appends data to items.
# Adding items into the stack
    def push(self, data):
        self.items.append(data)
        
# The method pop pops the first element in items
# Removing an element from the stack
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
#select operation
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do?\n ').split()
 
    operation = do[0].strip().lower()
     ##Pushes a element to top of the stack
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        ##Checks whether the stack is empty 
        if s.is_empty():
            print('Stack is empty.')
        ##Pops the top element
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
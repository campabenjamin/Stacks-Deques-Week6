class Empty(Exception):
    def __init__(self, message="An error occurred"):
        super().__init__(message)

class ArrayStack:
    # Creates an empty stack.
    def __init__(self):
        self.__data = []

    # Returns the number of elements in the stack.
    def __len__(self):
        return len(self.__data)
    
    # Returns True if stack is empty.
    def is_empty(self):
        return len(self.__data) == 0
    
    #Adds an element to the top of the stack.
    def push(self, element):
        self.__data.append(element)

    # Returns (but does not remove) the element at the top of the stack.
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self.__data[-1]
    
    # Removes and returns the element from the top of the stack (LIFO)
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self.__data.pop()
    
    # Returns the stack as a list.
    def get_stack(self):
        return self.__data
    
    def print_info(self):
        print(self.__data)
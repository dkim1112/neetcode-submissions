class MinStack:

    # Look into their return types!!
    
    def __init__(self):
        # initialization when MinStack is called
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # since minStack always keep track of mins,
        # save val OR smallest value already in minStack - whichever is smaller
        if self.minStack:
            val = min(val, self.minStack[-1])
        
        # append that to minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

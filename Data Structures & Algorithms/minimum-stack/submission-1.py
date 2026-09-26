import heapq
class MinStack:

    def __init__(self): 
        self.stack = [] 
        self.minimumStack = [] 
        

    def push(self, val: int) -> None:  
        self.stack.append(val)  
        if len(self.minimumStack) == 0 or self.minimumStack[0] >= val:  
            heapq.heappush(self.minimumStack, val)

    def pop(self) -> None: 
        element = self.stack.pop() 
        if element == self.getMin(): 
            heapq.heappop(self.minimumStack)

    def top(self) -> int: 
        return self.stack[-1]
        

    def getMin(self) -> int: 
        return self.minimumStack[0]
        

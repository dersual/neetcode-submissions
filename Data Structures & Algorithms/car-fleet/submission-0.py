class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        if len(position) == 1: 
            return 1 
        
        stack = []  
        pairs = sorted([[p, s] for p, s in zip(position, speed)], reverse=True)  
        timeToTarget = list(map(lambda x: (target - x[0]) / x[1], pairs))  

        for i in timeToTarget: 
            if stack and i <= stack[-1]:
                continue 
            else: 
                stack.append(i) 
        return len(stack)
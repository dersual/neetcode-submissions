class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures) 
        stack = [] 

        for i in range(len(temperatures)):  
            while stack and temperatures[stack[-1]] < temperatures[i]: 
                prevIndex = stack.pop()
                ret[prevIndex] = i - prevIndex 
            stack.append(i) 
        
        return ret
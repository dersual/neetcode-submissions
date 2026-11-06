class Solution:
    def isValid(self, s: str) -> bool:
        match = { 
            "(": ")", 
            "{": "}", 
            "[": "]"
        }   
        stack = [] 

        for c in s: 
            if c == "(" or c == "{" or c == "[": 
                stack.append(c) 
            elif len(stack) == 0: 
                return False 
            else: 
                element = stack.pop() 
                if match[element] != c:
                    return False  
        
        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:  
        map_dict = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for c in s:  
            if c == '[' or c == '(' or c == '{':  
                stack.append(c) 
            elif len(stack) == 0 or c != map_dict[stack[-1]]: 
                return False 
            else: 
                stack.pop()  
        if len(stack) != 0: 
            return False 

        return True

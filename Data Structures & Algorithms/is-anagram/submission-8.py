from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int) 
        t_dict = defaultdict(int)  

        if len(s) != len(t): 
            return False

        for c in s: 
            s_dict[c] += 1 
        
        for c in t: 
            t_dict[c] += 1
        

        for key, value in s_dict.items(): 
            if key not in t_dict:  
                return False 
            
            if value != t_dict[key]:
                return False 
        

        return True
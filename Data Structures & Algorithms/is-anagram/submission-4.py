class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if (len(s) != len(t)): 
            return False   
        s_dict = {}
        t_dict = {} 

        for char in s: 
            if s_dict.get(char, False) == False: 
                s_dict[char] = 1 
            else: 
                s_dict[char] += 1
        
        for char in t: 
            if t_dict.get(char, False) == False: 
                t_dict[char] = 1 
            else: 
                t_dict[char] +=1 
        
        for key in s_dict.keys(): 
            if (key not in t_dict or t_dict[key] != s_dict[key]): 
                return False
        return True 
        
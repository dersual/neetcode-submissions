class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False 
        hashSum1 = 0 
        hashSum2 = 0  
        i = 0 
        for i in range(0, len(s)): 
            hashSum1 += hash(s[i]) 
            hashSum2 += hash(t[i]) 
        return hashSum1 == hashSum2
        
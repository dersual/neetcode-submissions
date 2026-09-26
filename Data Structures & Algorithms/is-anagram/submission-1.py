class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t): 
            return False 
        hashSum1 = 0 
        hashSum2 = 0 
        index = 0 
        for index in range(0, len(s)): 
            hashSum1 += hash(s[index]) 
            hashSum2 += hash(t[index]) 
        return hashSum1 == hashSum2
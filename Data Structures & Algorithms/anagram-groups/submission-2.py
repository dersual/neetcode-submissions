class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagramDict = {} 
        for s in strs:  
            hashSum = 0 
            for ch in s: 
                hashSum+= hash(ch) 
            if hashSum in anagramDict: 
                anagramDict[hashSum].append(s) 
            else: 
                anagramDict[hashSum] = [s]  
        ret = []
        for key in anagramDict:  
            ret.append(anagramDict[key]) 
        return ret


        
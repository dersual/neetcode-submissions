class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        storedDict = {} 
        ret = []
        for string in strs:   
            hashSum = 0   
            for char in string: 
                hashSum += hash(char) 
            if not storedDict.get(hashSum, False): 
                storedDict[hashSum] = [string] 
            else: 
                storedDict[hashSum].append(string) 
        
        for group in storedDict.values(): 
            ret.append(group)  
        return ret
        



        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        retDict = {}
        for num in nums:  
            if not retDict.get(num, False): 
                retDict[num] = 1 
            else: 
                retDict[num] += 1  
        retArr = [] 
        i = 0  
        for i in range(0, k): 
           currentMax = max(retDict, key = retDict.get) 
           retArr.append(currentMax) 
           del retDict[currentMax] 
           
        return retArr
        
        
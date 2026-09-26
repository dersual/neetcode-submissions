import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        freqDict = {} 
        for num in nums: 
            freqDict[num] = freqDict.get(num, 0) + 1 
        
        pq = []
        for key, freq in freqDict.items():   
            heapq.heappush(pq, [freq, key]) 
            
            if len(pq) > k: 
                heapq.heappop(pq)
        
        ret = []  
        while pq: 
            element = heapq.heappop(pq)[1] 
            ret.append(element)  
        
        return ret

             
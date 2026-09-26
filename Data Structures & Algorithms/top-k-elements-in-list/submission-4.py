from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        freq_map = Counter(nums)  
        bucket = [None] * (len(nums) + 1) 

        for key, val in freq_map.items(): 
            
            if bucket[val]: 
                bucket[val].append(key) 
            else: 
                bucket[val] = [key] 

        
        filteredBucket = list(filter(lambda x: x != None, bucket)) 

        i = k 
        j = len(filteredBucket) - 1  
        result = [] 

        while i > 0 and j >= 0:   

            for element in filteredBucket[j]:
                result.append(element) 

                i -= 1 

                if i == 0:  
                    break  
            j -= 1 

        return result 



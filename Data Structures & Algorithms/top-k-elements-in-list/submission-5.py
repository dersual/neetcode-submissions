class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bucket = [[] for _ in range(len(nums) + 1)] 
        counts = Counter(nums) 
        ret = []
        for count in counts: 
            freq_bucket[counts[count]].append(count) 
        
        for i in range(len(freq_bucket) - 1, -1, -1):  
            j = 0
            while j < len(freq_bucket[i]):  
                ret.append(freq_bucket[i][j]) 
                if len(ret) == k: 
                    return ret 
                j+= 1 
        

        return ret
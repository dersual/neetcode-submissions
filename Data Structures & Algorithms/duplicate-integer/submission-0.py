class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:  
        dict = {}
        for x in nums: 
            if dict.get(x, False): 
                return True 
            else: 
                dict[x] = True 
        return False 

        
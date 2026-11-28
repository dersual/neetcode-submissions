class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  

        acc = 1
        for i in range(1, len(nums)):  
            acc *= nums[i-1] 
            res[i] = acc 
        
        acc = 1 
        for i in range(len(nums) - 2, -1, -1): 
            acc *= nums[i+1] 
            res[i] *= acc  
        
        return res
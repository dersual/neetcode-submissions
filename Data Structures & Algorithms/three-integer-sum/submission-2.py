class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        ret = [] 

        for i in range(len(nums)): 
            if nums[i] > 0: 
                continue  
            
            if i > 0 and nums[i-1] == nums[i]: 
                continue 
            
            left = i + 1 
            right = len(nums) - 1 
            while left < right:  
                res = nums[i] + nums[left] + nums[right] 
                if res < 0:
                    left += 1 
                elif res > 0: 
                    right -= 1  
                else: 
                    ret.append([nums[i], nums[left], nums[right]])    
                    left += 1 
                    right -= 1 
                    while left < right and nums[left] == nums[left-1]:
                        left+= 1 
                    
        
        return ret



            
            
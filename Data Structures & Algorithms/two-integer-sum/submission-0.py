class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        if len(nums) == 2: 
            return [0, 1]  
        dictNums = {nums[0]: 0} 
        i = 1 
        for i in range(i, len(nums)): 
            subtracted = target - nums[i] 
            if dictNums.get(subtracted, False) is False:   
                dictNums[nums[i]] = i 
            else: 
                return [dictNums[subtracted], i] 
        
        
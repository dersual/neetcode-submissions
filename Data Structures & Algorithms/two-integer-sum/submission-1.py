class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        passedDict = {} 
        i = 0 
        for i in range(0, len(nums)): 
            subtractedVal = target - nums[i]  
            print(passedDict)
            if passedDict.get(subtractedVal, False) or passedDict.get(subtractedVal, False) is 0: 
                return [passedDict[subtractedVal], i] 
            else: 
                passedDict[nums[i]] = i 

        
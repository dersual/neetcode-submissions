class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        
        set_nums = set(nums)  
        max_streak = 1
        for num in nums: 
            if num - 1 in set_nums: 
                continue  
            
            current_streak = 1
            while num + current_streak in set_nums:  
                current_streak += 1 
            
            if current_streak > max_streak:
                max_streak = current_streak 
        
        return max_streak


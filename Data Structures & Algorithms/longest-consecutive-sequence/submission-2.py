class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        if len(nums) == 0: 
            return 0 

        set_num = set(nums)  
        
        max_streak = 0 
        for num in set_num: 

            if num - 1 in set_num: 
                continue 
            
            streak = 1

            while num + streak in set_num:
                streak += 1 
            
            max_streak = max(streak, max_streak)  
        
        return max_streak



        
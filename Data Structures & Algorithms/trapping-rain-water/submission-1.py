class Solution:
    def trap(self, height: List[int]) -> int: 
        if len(height) == 0: 
            return 0 
        
        ret = 0 
        left = 0 
        right = len(height) - 1 
        left_max = height[left] 
        right_max = height[right] 

        while left < right:  
            if left_max <= right_max: 
                ret += left_max - height[left]  
                left += 1  
                left_max = max(height[left], left_max)
            else: 
                ret += right_max - height[right] 
                right -= 1   
                right_max = max(height[right], right_max)

        return ret

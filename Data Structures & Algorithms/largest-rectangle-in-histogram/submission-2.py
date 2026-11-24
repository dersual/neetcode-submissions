class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        stack = [] 

        for i in range(len(heights)):  
            currI = i
            while stack and stack[-1][0] >= heights[i]: 
                area = stack[-1][0] * (i - stack[-1][1]) 
                max_area = max(max_area, area)  
                currI = stack.pop()[1]   
                
            stack.append([heights[i], currI]) 
        
        for i in range(len(stack)):   
            area = stack[i][0] * (len(heights) - stack[i][1])   
            max_area = max(max_area, area)  

        return max_area
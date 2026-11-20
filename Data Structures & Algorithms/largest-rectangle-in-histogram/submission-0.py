class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] 

        for i in range(len(heights)):  
            currentI = i
            while stack and stack[-1][1] > heights[i]:  
                prev = stack.pop()
                area = prev[1] * (i - prev[0]) 
                maxArea = max(maxArea, area)
                currentI = prev[0]
                continue 
            stack.append([currentI, heights[i]]) 
        
        while stack: 
            prev = stack.pop() 
            area = prev[1] * (len(heights) - prev[0])  
            maxArea = max(area, maxArea) 
        
        return maxArea
        
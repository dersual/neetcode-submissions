class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        countsDict = {}  
        bucket = [[] for _ in range(len(nums))] 
        for num in nums: 
            if num in countsDict: 
                countsDict[num] += 1 
            else: 
                countsDict[num] = 1 

        for key in countsDict:  
            order = len(nums) - countsDict[key] 
            bucket[order].append(key) 

        ret = [] 
        numLeft = k  
        print(bucket)
        while numLeft > 0: 
            for grouping in bucket:  
                for num in grouping:  
                    ret.append(num)
                    numLeft-=1  
                    if numLeft == 0: 
                        break; 
                if numLeft == 0: 
                    break;
        return ret 


        
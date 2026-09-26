class Solution:

    def encode(self, strs: List[str]) -> str: 
        ret = ""  
        for s in strs: 
            ret += str(len(s)) + "#"  + s
        return ret 

    def decode(self, s: str) -> List[str]: 
        ret = []
        i = 0 
        while(i < len(s)): 
            lengthOfStr = "" 
            j = i  
            while s[j] != "#":  
                print(s[j], j, s)
                lengthOfStr += s[j]
                j+=1   
            # 5#hello 
            print(lengthOfStr)
            lengthOfStr = int(lengthOfStr) 
            i = j + 1 + lengthOfStr
            stringToTake = s[j+1:i] 
            ret.append(stringToTake)  
        return ret 



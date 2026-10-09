class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = "" 
        for s in strs: 
            delimiter = f"{len(s)}#" 
            ret += delimiter + s 
        
        return ret

    def decode(self, s: str) -> List[str]: 
        ret = []  
        i = 0  
        length = "" 
        while i < len(s):   
            if s[i] == "#":   
                print(length)
                numLength = int(length)
                ret.append(s[i+1:i+1+numLength]) 
                i += (numLength+1)   
                length = ""
            else:    
                length += s[i] 
                i += 1 


        return ret 


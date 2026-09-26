class Solution: 


    def encode(self, strs: List[str]) -> str:   
        result = ""
        for s in strs:  
            result += f"{len(s)}#{s}"  
        return result 

    def decode(self, s: str) -> List[str]:
        result = []  
        i = 0 
        j = 0  
        length = ""
        print(s)
        while i < len(s): 
            if s[i] != "#":   
                length += s[i]   
                i += 1
            else:   
                j = i + 1  
                decoded_str = "" 
                int_length = int(length) 
                while j < len(s) and j <= i + int_length: 
                    decoded_str += s[j]    
                    j+=1    
                result.append(decoded_str) 
                i = j     
                length = ""

        return result 
                
            
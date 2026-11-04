class Solution:

    def encode(self, strs: List[str]) -> str: 
        ret = "" 
        for s in strs:  
            ret += f"{len(s)}#{s}" 
        
        return ret 

    def decode(self, s: str) -> List[str]:   
        ret = []
        i = 0  
        length = ""

        while i <= len(s) - 1:   
            
            if s[i] != "#":  
                length += s[i]
                i += 1 
                continue 
            
            num_length = int(length) 
            j = i + 1  
            substr = s[j:j+num_length] 
            ret.append(substr) 
            length = "" 
            i = j + num_length 
        
        return ret

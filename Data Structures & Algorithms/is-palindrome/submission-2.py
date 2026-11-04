class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cleaned_s = "".join(filter(str.isalnum, s)) 

        left = 0 
        right = len(s) - 1 

        while left <= right:  
            if not str.isalnum(s[left]): 
                left += 1 
            elif not str.isalnum(s[right]):  
                right -= 1  
            elif s[left].lower() != s[right].lower(): 
                print((s[left].lower(), left), (s[right].lower(), right))
                return False    
            else: 
                left += 1 
                right -= 1
        

        return True

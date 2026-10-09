class Solution:
    def isPalindrome(self, s: str) -> bool: 
        filteredS = "".join(char.lower() for char in s if char.isalnum())
        i = 0 
        j = len(filteredS) - 1
        while i <= j:   
            if filteredS[i].lower() != filteredS[j].lower(): 
                return False  
            i+=1 
            j-=1 
        return True
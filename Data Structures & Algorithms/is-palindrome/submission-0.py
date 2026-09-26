class Solution:
    def isPalindrome(self, s: str) -> bool: 

        cleaned_s = "".join(filter(str.isalnum, s.lower()))
        for index, char in enumerate(cleaned_s): 
          reverseIndex = len(cleaned_s) - index - 1 

          if cleaned_s[index] != cleaned_s[reverseIndex]: 
            return False 
        
        return True

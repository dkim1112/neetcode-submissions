class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string first
        s = "".join(char.lower() for char in s if char.isalnum())
        
        left, right = 0, len(s) - 1
        # isalnum() method returns True if all the characters are alphanumeric
        # meaning alphabet letter (az) and numbers (0-9).
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
            
        

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string first
        s = "".join(char.lower() for char in s if char.isalnum())
        
        left, right = 0, len(s) - 1
        # utilize .isalnum() to eliminate all non-alphabet and case sensitivity

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        # making it a set to be able to add/remove
        charSet = set()
        left = 0 # left pointer

        # i = right pointer
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            count = max(count, i - left + 1)

        return count
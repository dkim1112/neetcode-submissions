class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using hashset to find duplicates
        
        # only need to run once (O(N))
        seen = set()

        for num in nums:
            if num in seen:
                return num # that number is duplicate
            seen.add(num)
        
        return -1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left, right = 0, k - 1

        while right < len(nums):
            maxi = float('-infinity')
            for i in range (left, right + 1):
                maxi = max(maxi, nums[i])
                
            ans.append(maxi)
            left += 1
            right += 1
        
        return ans

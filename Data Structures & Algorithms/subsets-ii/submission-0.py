class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def rec(i, subset):
            # base case
            if i == len(nums):
                res.append(subset[::])
                return
            
            # recursion - try add
            subset.append(nums[i])
            rec(i+1, subset)

            # recursion - try pop
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            rec(i+1, subset)
        
        rec(0, [])
        return res
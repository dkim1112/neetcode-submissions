class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # start with empty arr (that itself counts as one)

        for num in nums:
            new_subset = []

            for subset in res:
                new_subset.append(subset + [num])
            
            res.extend(new_subset)
            
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # start with empty arr (that itself counts as one)

        for num in nums:
            new_subset = []

            for subset in res:
                # ex.) subset = [1,2]
                # ex.) [num] = [3]
                # result = [1, 2, 3]
                new_subset.append(subset + [num])
            
            res.extend(new_subset) # not .append
            
        return res
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since sorted in ascending order,
        # we can split and assign right / left based on where target sits

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1
    
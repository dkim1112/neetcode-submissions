class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # whats hard: since it isn't strictly increasing (bc rotated)
        # we need to first find where that split happens

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # base case
            if nums[m] == target:
                return m
            
            # due to rotation, for left sorted
            if nums[l] <= nums[m]:
                # if target is b/w left ~ m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # if target is b/w m ~ right
                else:
                    l = m + 1
            # for right sorted
            else:
                # if target is b/w m ~ right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # if target is b/w left ~ m
                else:
                    r = m - 1
        
        # if nothing gets returned
        return -1



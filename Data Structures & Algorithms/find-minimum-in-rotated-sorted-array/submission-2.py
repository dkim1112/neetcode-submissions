class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if it was already sorted ascending, it maintains that pattern
        # it's just that the starting point differs
        # we just need to find how many time it was rotated => that num as idx = min

        res = 99999
        start, end = 0, len(nums) - 1

        while start <= end:
            # if basically no rotation happened (= 해도 원상복귀인 상태라면)
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

        
            m = (start + end) // 2
            res = min(res, nums[m])

            # if it is NOT already sorted, apply this pattern.
            if nums[m] >= nums[start]:
                # left half (start ~ m) is sorted (ex. 3, 4, 5 (m)... 1, 2)
                # move search more towards right 
                start = m + 1
            else:
                end = m - 1
        
        return res

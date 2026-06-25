class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Base Cases
            if total == target:
                res.append(cur.copy()) # use copy of it because this cur is continuosly used later on
                return
            if i >= len(nums) or total > target:
                return

            # Recursive (include / skip)

            # include
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # skip
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
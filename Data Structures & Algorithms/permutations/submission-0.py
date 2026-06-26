class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(cur):
            # base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
        
            # recursion (trust the recursion)
            for i in range(len(nums)):
                if used[i]:
                    continue
                else:
                    cur.append(nums[i])
                    used[i] = True

                    dfs(cur)

                    cur.pop()
                    used[i] = False
                
        dfs([])
        return res
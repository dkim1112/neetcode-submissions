class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 2 strategies: Sort & Backtracking
        res = []
        # sort array so duplicates are next to each other
        candidates.sort()

        def dfs(i, cur, total):
            # base cases
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # recursion - option 1: try adding
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i]) #i+1 bc each num can only be used at MOST once
            
            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # list of valid palindromes
        temp = [] # only store palindrome

        # traverse from left ~ right, and make partitions
        # at any idx i, we ask: "do I cut here / or continue?" => backtrack
        def dfs(i):
            # base case
            if i >= len(s):
                res.append(temp.copy())
                return
            
            # recursion
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    temp.append(s[i : j+1]) # try going one more
                    dfs(j+1)
                    temp.pop() # for next one
            
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        return True
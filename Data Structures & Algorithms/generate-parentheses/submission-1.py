class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we can add "(" only if open < n 
        # we can add ")" only if close < open
        # complete when open == close == n
        stack = []
        res = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            # 항상 backtrack은 추가하고 빼줘야함
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0,0)
        return res
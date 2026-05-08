class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        
        # every operator applies two most recent values that come before.
        # by processing expression from end, 
        # when we see number -> just return that number
        # when we see operator -> evaluate the two values that belong to it

        # number = base case / operator = recursive call

        def dfs():
            curr = tokens.pop()
            if curr not in "+/*-":
                return int(curr)
            
            right = dfs()
            left = dfs()

            if curr == "+":
                return left + right
            elif curr == "-":
                return left - right
            elif curr == "*":
                return left * right
            else:
                return int(left / right)

        return dfs()

            
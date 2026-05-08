class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # lets try brute force
        stack = []

        # 계속 2개 pop 하고 result를 append하니까,
        # 기존에 stack에 쌓여있던 숫자들은 다 없어지고 stack[0]에 result만 남게 됨.
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
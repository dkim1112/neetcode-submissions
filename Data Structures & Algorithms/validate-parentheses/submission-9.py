class Solution:
    def isValid(self, s: str) -> bool:
        # save 해뒀다가 나중에 (순서에 맞게) 잘 닫히는지 확인해봐야 함.
        # 가능한 조합들을 저장해뒀다가, 닫혔을때 (= 하나의 pair 완성되면) - valid한지 검증
        # 들어간 순서대로 뺄 수 있어야 함 = STACK

        stack = []
        valid = ["()", "{}", "[]"]

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])

            # means likely one of the closing ones            
            else:
                if len(stack) == 0:
                    return False
                trying = stack.pop() + s[i]

                if trying not in valid:
                    return False
                # else라고 해서 True를 바로 뱉으면 안되는게, we need to check all
                
        return len(stack) == 0


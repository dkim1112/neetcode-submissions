class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp돌면서 대기자 명단을 만듬.
        # 이 대기자들은 본인보다 따듯한 온도가 나오면, 나갈 수 있고
        # 나갈때 idx 차이를 저장해둔다.

        res = [0] * len(temperatures)
        # stack: keeps track of temperatures that are still waiting for a warmer day.
        stack = [] # as pairs: [temp, index]

        # iterate through temp for each available spot in res
        for i, temp in enumerate(temperatures):
            # top of stack: stack[-1][0]
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        
        return res


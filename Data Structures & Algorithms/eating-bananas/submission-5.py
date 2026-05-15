class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end

        # 이 l ~ r을 다 돌리기엔 시간이 너무 오래걸리니, binary search 적용
        while start <= end:
            possible = (start + end) // 2 # idx of middle
            totalTime = 0
            # totalTime calculation
            for p in piles:
                totalTime += math.ceil(float(p) / possible)

            # if this is true, we can even try a smaller #
            if totalTime <= h:
                res = possible
                end = possible - 1
            else:
                # dont need to save to res, bc not valid value
                start = possible + 1

        return res
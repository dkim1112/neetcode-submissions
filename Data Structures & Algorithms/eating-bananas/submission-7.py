class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end

        # 1부터 영원히 하나 나올때까지 돌려보는것도 방법 = brute force
        # 근데 우리에겐 너무나도 당연한 possible 최대치가 있음. = piles의 항목 중 max.
        # set that as a boundary and start.

        # 이 start ~ end를 다 돌리기엔 시간이 너무 오래걸리니, binary search 적용
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
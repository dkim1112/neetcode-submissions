class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # array of int "stones", stones[i] = weight of ith stone
        
        # each step, choose 2 heaviest stones, with weight x, y
        # smash two together
        # if x == y, both destroyed
        # if x < y, w destroyed & y weight = y - x

        # continue until <= 1 stone left
        # return weight of last stone or 0 if none

        # via max-heap (heapify), we keep the biggest at top.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: # not if (because continuosly removed & added)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x - y) # adding back in new y (with new weight)
            
        stones.append(0)
        return abs(stones[0])

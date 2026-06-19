class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # array of int "stones", stones[i] = weight of ith stone
    
        


        # via max-heap (heapify), we keep the biggest at top.
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # continue until <= 1 stone left
        while len(stones) > 1: # not if (because continuosly removed & added)
            # each step, choose 2 heaviest stones, with weight x, y / smash two together
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            # if x == y, both destroyed
            # if x < y, w destroyed & y weight = y - x
            if x < y:
                diff = x - y # remember, they're stored in negative int!
                heapq.heappush(stones, diff) # adding back in new y (with new weight)
            
        # return weight of last stone or 0 if none

        return abs(stones[0]) if stones else 0
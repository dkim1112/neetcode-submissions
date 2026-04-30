class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # want to buy it when its cheapest
        # want to sell it when its most expensive
        # sell 하는 시점은 꼭 buy 하고 나서

        l, r = 0, len(prices) - 1

        currMax = 0
        while l < r:
            left = prices[l]
            maxPriceInRange = max(prices[l + 1:])
            
            if maxPriceInRange - left > currMax:
                currMax = maxPriceInRange - left
            
            l += 1
        
        return currMax
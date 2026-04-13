class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 20 10 20 20 3 100
        #             l  r
        l = 0

        maxProfit = 0

        for r in range(1, len(prices)):
            temp = prices[r] - prices[l]
            
            if temp > 0:
                maxProfit = max(temp, maxProfit)
            elif temp < 0:
                l = r
        return maxProfit
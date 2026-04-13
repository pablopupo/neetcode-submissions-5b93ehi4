class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10, 1, 5, 6, 7, 1]
        
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
                r += 1
        
        return maxProfit
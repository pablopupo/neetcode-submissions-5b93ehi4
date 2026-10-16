class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            if prices[l] < prices[r]: 
                price = prices[r] - prices[l]
                ans += price
            l += 1
            r += 1
        return ans

        
        
        
        
        
        
      
        


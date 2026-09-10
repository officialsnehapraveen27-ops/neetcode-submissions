class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left=0
        right=1
        n = len(prices)
        maxprofit=0
        while right < n:

            if prices[left] < prices[right]:

                profit = prices[right] - prices[left]

                maxprofit=max(maxprofit, profit)

                

            else:

                left=right
            
            right+=1
        
        return maxprofit
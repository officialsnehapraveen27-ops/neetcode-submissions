class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_index, max_index=0,0
        max_profit=0
        n= len(prices)
        for i in range(n):

            if prices[i] < prices[min_index]:

                min_index=i
                max_index=i
            
            if prices[i] > prices[max_index]:

                max_index = i 

            if max_index >= min_index:

                max_profit= max(max_profit, prices[max_index] - prices[min_index])

        return max_profit
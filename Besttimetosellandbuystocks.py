class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = max(prices)
        for i in range(len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice

        return maxprofit

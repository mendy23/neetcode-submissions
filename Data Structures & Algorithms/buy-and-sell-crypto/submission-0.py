class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in [0, 1]:
            return 0

        sortedPrices = sorted(prices, reverse=True)
        maxProfit = 0
        priceMap = {x: i for i, x in enumerate(prices)}

        for j in range(len(prices)):
            for k in range(len(prices)):
                if j < priceMap[sortedPrices[k]] and sortedPrices[k] > prices[j]:
                    profit = sortedPrices[k] - prices[j]
                    if profit > maxProfit:
                        maxProfit = profit
                k +=1
            j += 1
        
        return maxProfit

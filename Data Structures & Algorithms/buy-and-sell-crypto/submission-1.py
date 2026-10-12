class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in [0, 1]:
            return 0
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        for j in range(len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # NeetCode solution
        buy, profit = prices[0], 0

        for i in range(1, len(prices), 1):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])

        return profit
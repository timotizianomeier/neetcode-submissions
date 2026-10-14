class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP solution
        if len(prices) < 1:
            return 0

        buy, profit = prices[0], 0

        for i in range(1, len(prices), 1):
            profit = max(profit, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]

        return profit
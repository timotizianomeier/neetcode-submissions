class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force O(n^2)
        best = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices), 1):
                best = max(best, prices[j] - prices[i])

        return best
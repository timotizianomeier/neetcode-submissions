class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer solution
        
        best = 0
        i, j = 0, len(prices) - 1
        while i < j:
            best = max(best, prices[j] - prices[i])
            if prices[i+1] < prices[i]:
                i += 1
            elif prices[j-1] > prices[j]:
                j -= 1
            else:
                i += 1

        return best
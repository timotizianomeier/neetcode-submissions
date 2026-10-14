class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer solution
        if len(prices) < 2:
            return 0

        buy, sell = (prices[0], 0), (prices[1], 1)
        print(f"initial buy is {buy}")
        print(f"initial sell is {sell}")

        for i in range(len(prices) - 1):
            j = i + 1
            print(f"we are at i = {i} and j = {j}")
            if prices[j] > sell[0] and j > buy[1]:
                sell = (prices[j], j)
                print(f"sell is updated, now: {sell}")
            if prices[i] < buy[0] and i < sell[1]:
                buy = (prices[i], i)
                print(f"buy is updated, now: {buy}")

        print(f"final buy is {buy}")
        print(f"final sell is {sell}")

        return max(sell[0] - buy[0], 0)
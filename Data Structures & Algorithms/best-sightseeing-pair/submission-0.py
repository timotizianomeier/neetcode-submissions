class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = -1
        for i in range(len(values)):
            for j in range(len(values)):
                if i < j:
                    best = max(best, values[i] + values[j] - (j - i))

        return best
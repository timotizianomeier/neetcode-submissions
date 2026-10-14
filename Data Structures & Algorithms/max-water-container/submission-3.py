class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n)
        best = 0
        r = len(heights)-1
        for l in range(len(heights)):
            if l < r:
                best = max(best, (r - l) * min(heights[l], heights[r]))
                if heights[l] < heights[r]:
                    continue
                else:
                    r -=1

        return best
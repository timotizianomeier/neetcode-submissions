class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force O(n^2)
        best = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights), 1):
                height = min(heights[l], heights[r])
                width = r - l
                current = height * width
                best = max(best, current)

        return best
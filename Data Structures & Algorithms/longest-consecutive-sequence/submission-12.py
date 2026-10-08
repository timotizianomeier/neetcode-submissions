class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # NeetCode solution version
        values = set(nums)
        best = 0

        for num in values:
            if num-1 not in values:
                current = 1
                while num+current in values:
                    current += 1
                best = max(current, best)

        return best
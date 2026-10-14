class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # better time complexity
        values = set(nums)
        if len(nums) == 0:
            return 0
        best, current = 1, 1

        for i in range(len(nums)):
            if nums[i]-1 not in values:
                continue
            current = 1
            for j in range(i, len(nums), 1):
                if nums[j]+1 in values:
                    current += 1
                best = max(current, best)

        return best
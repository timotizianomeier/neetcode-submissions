class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # NeetCode solution version
        values = set(nums)
        if len(nums) == 0:
            return 0
        best = 0

        for i in range(len(nums)):
            if nums[i]-1 not in values:
                current = 1
                val = nums[i]
                while val+current in values:
                    current += 1
                best = max(current, best)

        return best
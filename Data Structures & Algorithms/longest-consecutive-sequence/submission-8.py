class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # better time complexity
        values = set(nums)
        if len(nums) == 0:
            return 0
        best, current = 1, 1

        for i in range(len(nums)):
            if nums[i]-1 not in values:
                current = 1
                val = nums[i]
                while val+1 in values:
                    current += 1
                    best = max(current, best)
                    val += 1

        return best
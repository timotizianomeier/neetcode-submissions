class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first naive solution
        if len(nums) == 0:
            return 0

        nums.sort()
        print(nums)
        best, current = 1, 1
        for i in range(1, len(nums), 1):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
                if current > best:
                    best = current
            else:
                current = 1
        return best
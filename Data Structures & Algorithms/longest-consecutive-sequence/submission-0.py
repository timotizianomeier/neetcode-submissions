class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first naive solution
        nums.sort()
        print(nums)
        best, current = 0, 1
        for i in range(1, len(nums), 1):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
                if current > best:
                    best = current
            else:
                current = 0
        return best
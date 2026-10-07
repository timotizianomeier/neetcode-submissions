class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive solution
        left, right = [1] * len(nums), [1] * len(nums)

        i = 1
        while i < len(nums):
            left[i] = nums[i-1] * left[i-1]
            i += 1

        i = len(nums) - 2
        while i >= 0:
            right[i] = nums[i+1] * right[i+1]
            i -= 1

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res
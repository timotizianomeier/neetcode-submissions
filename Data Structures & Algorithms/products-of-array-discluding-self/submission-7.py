class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # NeetCode solution
        res = [1] * len(nums)

        i, prefix = 1, 1
        while i < len(nums):
            prefix *= nums[i-1]
            res[i] *= prefix
            i += 1

        i, postfix = len(nums) - 2, 1
        while i >= 0:
            postfix *= nums[i+1]
            res[i] *= postfix
            i -= 1
        
        return res
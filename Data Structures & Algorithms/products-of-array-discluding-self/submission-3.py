class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive solution
        total, res = 1, [0] * len(nums)
        
        for n in nums:
            total *= n

        for i in range(len(nums)):
            res[i] = total
            if nums[i] != 0:
                res[i] //= nums[i]

        return res
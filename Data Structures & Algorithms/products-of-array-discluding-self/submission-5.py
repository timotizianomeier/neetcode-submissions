class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive solution, O (n^2)
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j != i:
                    total *= nums[j]
            res[i] = total

        return res
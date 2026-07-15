class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force, O(n^2)
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    result[i] = result[i] * nums[j]
        return result
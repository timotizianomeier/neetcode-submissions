class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap, pre-filled
        hashMap = {}
        for i in range(len(nums)):
            hashMap[i] = nums[i]

        for i in range(len(nums)):
            diff = target - nums[i]
            if hashMap.get(nums[i]) == diff:
                return [i, hashMap.get(nums[i])]
        
        # brute force O(n^2)
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                j = j + 1
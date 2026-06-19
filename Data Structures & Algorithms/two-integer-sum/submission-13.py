class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap, not pre-filled, solution using enumerate
        hashMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                # we go from left to right, so i must come second for test cases to pass!
                return [hashMap.get(diff), i]
            else:
                hashMap.get(val, i)

        # HashMap, not pre-filled
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            # must not be the same index
            if hashMap.get(diff, -1) != -1: 
                if i != hashMap.get(diff):
                    if i < hashMap.get(diff):
                        return [i, hashMap.get(diff)]
                    else:
                        return [hashMap.get(diff), i]
        
        # brute force O(n^2)
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                j = j + 1
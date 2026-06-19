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
                hashMap[val] = i

        
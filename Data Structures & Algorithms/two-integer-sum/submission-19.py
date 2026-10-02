class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Improved version, do everything in a single loop
        # O(n) time and space
        # Version with different syntax for checking membership
        array = {}
        for j, val in enumerate(nums):
            diff = target - val
            if diff in array:
                return [array[diff], j]
            array[val] = j

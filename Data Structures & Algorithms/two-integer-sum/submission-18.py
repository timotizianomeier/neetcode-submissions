class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Improved version, do everything in a single loop
        # O(n) time and space
        array = {}
        for j, val in enumerate(nums):
            i = array.get(target - val, -1)
            if i != -1:
                return [i, j]
            array[val] = j

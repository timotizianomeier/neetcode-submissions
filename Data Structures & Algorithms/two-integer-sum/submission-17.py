class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {value: index for index, value in enumerate(nums)}
    
        for i in range(len(nums)):
            j = array.get(target-nums[i], -1)
            if j != -1 and j != i:
                return [i, j]

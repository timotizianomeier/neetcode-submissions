class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set()
        for i in range(len(nums)):
            if nums[i] in set_of_nums:
                return True
            set_of_nums.add(nums[i] )
        return False
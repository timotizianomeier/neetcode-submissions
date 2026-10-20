class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) solution attempt
        l, mid, r = 0, len(nums) // 2, len(nums) - 1
        while r - l > 1:
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid
            mid = (r - l) // 2 + l

        return nums[r]
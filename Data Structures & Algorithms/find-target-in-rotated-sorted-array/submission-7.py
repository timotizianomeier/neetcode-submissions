class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) solution attempt
        res = -1
        l, m, r = 0, len(nums) // 2, len(nums) - 1

        while l < r:
            if nums[m] == target:
                return m
            elif nums[l] < nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]:
                if nums[l] >= target and target >= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            m = (l + r) // 2

        return m if nums[m] == target else -1
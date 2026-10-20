class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial O(n) solution
        for i, num in enumerate(nums):
            if num == target:
                return i

        return -1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial O(n) solution
        res = 1001
        for num in nums:
            res = min(res, num)

        return res
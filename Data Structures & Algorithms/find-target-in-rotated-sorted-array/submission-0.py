class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial O(n) solution
        count = {}
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + i

        return count.get(target, -1)
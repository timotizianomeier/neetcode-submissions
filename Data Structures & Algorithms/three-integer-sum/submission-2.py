class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first naive solution
        index = {num: idx for idx, num in enumerate(nums)}
        res = set()

        for i in range(len(nums)):
            for j in range(len(nums) - 1, 0, -1):
                if i == j:
                    continue
                third = - nums[i] - nums[j]
                k = index.get(third, -10^6)
                if k == i or k == j:
                    continue
                if k != -10^6:
                    sol = tuple(sorted((nums[i], nums[j], nums[k])))
                    res.add(sol)

        return [item for item in res]
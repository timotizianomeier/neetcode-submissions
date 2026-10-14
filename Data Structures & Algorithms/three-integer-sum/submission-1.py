class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        res = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i == j or i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        sol = tuple(sorted((nums[i], nums[j], nums[k])))
                        res.add(sol)

        return [item for item in res]
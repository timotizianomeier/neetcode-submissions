class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1

        return sorted(hashMap, key = lambda x: hashMap[x], reverse = True)[:k]



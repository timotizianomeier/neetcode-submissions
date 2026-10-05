class Solution:
    # first O(n log n) attempt
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] = count[num] + 1

        count_sorted = [(key, value) for key, value in sorted(count.items(), reverse = True, key = lambda p: p[1])]

        return [item[0] for item in count_sorted[:k]]
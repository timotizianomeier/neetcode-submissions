class Solution:
    # O(n) solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = count[num] + 1

        for n, c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result


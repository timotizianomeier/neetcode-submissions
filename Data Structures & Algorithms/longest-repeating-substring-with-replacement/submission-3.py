class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first naive solution
        longest = 0

        if len(s) == 0:
            return longest

        freq = defaultdict(int)
        for i, ch in enumerate(s):
            freq.clear()
            j = i + 1
            freq[ch] += 1
            while j < len(s) and j - i - max(freq.values()) < k:
                freq[s[j]] += 1
                j += 1
            longest = max(longest, j - i + 1)

        return min(len(s), longest)
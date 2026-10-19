class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first naive solution
        longest = 0
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1

        return min(max(freq.values()) + k, len(s))
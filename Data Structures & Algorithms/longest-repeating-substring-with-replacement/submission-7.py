class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first naive solution
        longest = 0

        if len(s) == 0:
            return longest

        freq = defaultdict(int)
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while r - l + 1 - max(freq.values(), default = 0) > k:
                    freq[s[l]] -= 1
                    l += 1
            longest = max(longest, r - l + 1)

        return longest
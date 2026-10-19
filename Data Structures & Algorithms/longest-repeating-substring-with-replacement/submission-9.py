class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # NeetCode advanced solution
        freq = {}
        longest, l, maxF = 0, 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxF = max(maxF, freq[s[r]])
            while r - l + 1 - maxF > k:
                    freq[s[l]] -= 1
                    l += 1
            longest = max(longest, r - l + 1)

        return longest
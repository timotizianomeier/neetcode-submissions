class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first naive solution
        longest = 0

        if len(s) == 0:
            return longest

        freq = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            longest = max(longest, r - l + 1)
            if r - l + 1 - max(freq.values(), default = 0) <= k:
                freq[s[r]] += 1
                r += 1
            else:
                freq[s[l]] -= 1
                l += 1

        return longest
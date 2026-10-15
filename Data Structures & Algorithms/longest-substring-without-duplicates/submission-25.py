class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using hash table
        seen = {}
        start, longest = 0, 0
        for i, ch in enumerate(s):
            if seen.get(ch, -1) == -1:
                seen[ch] = i
            else:
                start = seen[ch] + 1
                seen[ch] = i
                continue
            longest = max(longest, i + 1 - start)

        return longest
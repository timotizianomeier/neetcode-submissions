class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using hash table
        seen = defaultdict(str)
        start, longest = 0, 0
        for i, ch in enumerate(s):
            longest = max(longest, i - start)
            if seen.get(ch, -1) == -1:
                seen[ch] = i
            else:
                seen[ch] = i
                start = i

        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using hash table
        # issue: somehow need to handle off by 1
        seen = defaultdict(str)
        start, longest = 0, 0
        for i, ch in enumerate(s):
            longest = max(longest, 1, i - start)
            if i < 2:
                longest += 1
            if seen.get(ch, -1) == -1:
                seen[ch] = i
            else:
                seen[ch] = i
                longest = max(longest, i - start)
                start = i

        return longest
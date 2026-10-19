class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force O(n^2)
        longest = 0
        for i, ch in enumerate(s):
            budget, current, j = k, 0, i
            while j < len(s):
                if s[j] != ch:
                    if budget > 0:
                        budget -= 1
                    else:
                        break
                current += 1
                j += 1
            longest = max(longest, current)

        return longest
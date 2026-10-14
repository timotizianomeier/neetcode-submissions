class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        best = 1
        for i in range(len(s)):
            seen = set()
            current = 1
            for j in range(i+1, len(s), 1):
                if s[j] in seen:
                    best = max(best, current)
                    break
                else:
                    seen.add(s[j])
                    current +=1
                    best = max(best, current)

        return best
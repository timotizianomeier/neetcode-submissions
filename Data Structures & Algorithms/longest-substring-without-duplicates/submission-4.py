class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        best, current = 0, 1
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            best = max(best, current)
            current = 1
            best = max(best, current)
            for j in range(i+1, len(s), 1):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    current +=1
                    best = max(best, current)

        return best
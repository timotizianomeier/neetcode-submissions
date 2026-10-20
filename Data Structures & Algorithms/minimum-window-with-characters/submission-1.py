class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first naive solution
        freqT = {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        l = 0
        freqS = {}
        left, right = 0, len(s) - 1

        for r, ch in enumerate(s):
            freqS[ch] = freqS.get(ch, 0) + 1
            while all(freqS.get(char, 0) >= count for char, count in freqT.items()):
                if r - l + 1 < right - left + 1:
                    left, right = l, r
                freqS[s[l]] -= 1
                l += 1

        if len(t) > len(s):
            return ""
            
        return s[left:right+1]
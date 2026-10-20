class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first naive solution
        freqT = {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        shortest = ""
        l = 0
        freqS = {}

        for r, ch in enumerate(s):
            freqS[ch] = freqS.get(ch, 0) + 1
            while all(freqS.get(char, 0) >= count for char, count in freqT.items()):
                shortest = s[l:r+1]
                freqS[s[l]] -= 1
                l += 1

        return shortest
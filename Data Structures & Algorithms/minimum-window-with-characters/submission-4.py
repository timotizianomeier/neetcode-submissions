class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # NeetCode solution
        if len(t) == 0: return ""

        freqT, freqS = {}, {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        need, have = len(freqT), 0
        l = 0
        res, resLen = [-1, -1], float("infinity")

        for r, ch in enumerate(s):
            freqS[ch] = freqS.get(ch, 0) + 1

            if ch in freqT and freqS[ch] == freqT[ch]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""
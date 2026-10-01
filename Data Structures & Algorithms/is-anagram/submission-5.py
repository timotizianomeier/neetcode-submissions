class Solution:
    # O(n + m)
    def isAnagram(self, s: str, t: str) -> bool:
        return self.turnIntoDict(s) == self.turnIntoDict(t)

    def turnIntoDict(self, s: str) -> dict:
        ana = {}
        for i in range(len(s)):
            ana[s[i]] = ana.get(s[i], 0) + 1
        return ana
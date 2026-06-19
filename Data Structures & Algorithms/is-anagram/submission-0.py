class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for i in s:
            hashS[i] = hashS.get(i, 0) + 1

        for i in t:
            hashT[i] = hashT.get(i, 0) + 1

        return hashS == hashT
        
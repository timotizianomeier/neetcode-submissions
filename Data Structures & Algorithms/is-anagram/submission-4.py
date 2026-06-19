class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted solution
        return sorted(s) == sorted(t)

        # leveraging Counter
        return Counter(s) == Counter(t)

        # explicit logic
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1

        for i in hashS:
            if hashS[i] != hashT.get(i, 0):
                return False

        return True

        # alternative explicit logic
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1

        return hashS == hashT
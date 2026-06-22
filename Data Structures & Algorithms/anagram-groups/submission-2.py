class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HashMap ith character counts for key, O(m*n)
        hashMap = {}
        for i, txt in enumerate(strs):
            counts = [0] * 26
            for ch in txt:
                counts[ord(ch) - ord('a')] = counts[ord(ch) - ord('a')] + 1
            if hashMap.get(tuple(counts), -1) != -1:
                hashMap[tuple(counts)].append(txt)
            else:
                hashMap[tuple(counts)] = [txt]
        return list(hashMap.values())
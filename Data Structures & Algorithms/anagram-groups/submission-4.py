class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution version
        hashMap = defaultdict(list) # so no ifelse block needed
        for i, txt in enumerate(strs):
            counts = [0] * 26
            for ch in txt:
                counts[ord(ch) - ord('a')] += 1
            hashMap[tuple(counts)].append(txt)
        return list(hashMap.values())
        
       
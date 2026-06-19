class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HashMap version, initial attempt
        hashMap = {}
        for i, txt in enumerate(strs):
            if hashMap.get(''.join(sorted(txt)), -1) == -1:
                hashMap[''.join(sorted(txt))] = [txt]
            else:
                hashMap[''.join(sorted(txt))].append(txt)
        return list(hashMap.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for s in strs:
            s_sort = ''.join(sorted(s))
            strings[s_sort].append(s)
        return list(strings.values())
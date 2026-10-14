class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force version, abandon and try directly with HashMap
        sorted_string = []
        for i in range(len(strs)):
            sorted_string.append(''.join(sorted(strs[i])))

        grouped_anagrams = []
        for i in range(len(sorted_string)):
            anagram = [strs[i]]
            j = i + 1
            while j < len(sorted_string):
                if sorted_string[i] == sorted_string[j]:
                    anagram.append(sorted_string[j])
                    sorted_string.pop(j)
                j = j + 1
            grouped_anagrams.append(anagram)
        
        return grouped_anagrams
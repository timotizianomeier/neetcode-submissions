class Solution:
    def isValid(self, s: str) -> bool:
        # first naive solution
        if len(s) % 2 != 0:
            return False

        count = defaultdict(int)
        for ch in s:
            count[ch] += 1

        if count['('] != count[')'] or count['['] != count[']'] or count['{'] != count['}']:
            return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # NeetCode solution
        s = s.lower()
        
        start, end = 0, len(s)-1

        while end > start:
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1 
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
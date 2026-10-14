class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(".", "")
        s = s.replace(",", "")
        
        start, end = 0, len(s)-1

        while end > start:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
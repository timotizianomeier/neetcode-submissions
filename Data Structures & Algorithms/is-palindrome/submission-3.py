class Solution:
    def isPalindrome(self, s: str) -> bool:
        # NeetCode brute force
        new = ""
        
        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        return new == new[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        # first naive solution
        if len(s) % 2 != 0:
            return False

        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if ch == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif ch == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif ch == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False

        return True
        
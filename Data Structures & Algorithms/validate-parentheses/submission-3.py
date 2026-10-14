class Solution:
    def isValid(self, s: str) -> bool:
        # first naive solution
        if len(s) % 2 != 0:
            return False

        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.insert(0, ch)
            else:
                if len(stack) == 0:
                    return False
                elif ch == ')' and stack[0] == '(':
                    stack.pop(0)
                elif ch == ']' and stack[0] == '[':
                    stack.pop(0)
                elif ch == '}' and stack[0] == '{':
                    stack.pop(0)
                else:
                    return False

        return True
        
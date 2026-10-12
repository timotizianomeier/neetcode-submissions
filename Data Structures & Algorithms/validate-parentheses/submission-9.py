class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                elif ch == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif ch == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif ch == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False

        return len(stack) == 0
        
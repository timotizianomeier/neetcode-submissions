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
                stack.append(ch)

        for ch in stack:
            if ch == '(' and stack[len(stack) - 1] == ')':
                stack.pop(0)
                stack.pop(len(stack) - 1)
            elif ch == '[' and stack[len(stack) - 1] == ']':
                stack.pop(0)
                stack.pop(len(stack) - 1)
            elif ch == '{' and stack[len(stack) - 1] == '}':
                stack.pop(0)
                stack.pop(len(stack) - 1)
            else:
                False

        return True
        
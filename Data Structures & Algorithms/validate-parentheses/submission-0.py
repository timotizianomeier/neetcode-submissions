class Solution:
    def isValid(self, s: str) -> bool:
        # first naive solution
        if len(s) % 2 != 0:
            return False

        opn, cls = [], []

        for ch in s:
            if ch == '(':
                opn.append(1)
            if ch == '[':
                opn.append(2)
            if ch == '{':
                opn.append(3)
            if ch == ')':
                cls.insert(0, 1)
            if ch == ']':
                cls.insert(0, 2)
            if ch == '}':
                cls.insert(0, 3)

        print(opn)
        print(cls)
        return opn == cls
        
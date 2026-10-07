class Solution:

    # First naive solution
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        
        while i < len(s):
            num = ""
            
            while s[i] != "#":
                num += s[i]
                i += 1

            i += 1
            count = int(num)
            word = ""

            for j in range(count):
                word += s[i]
                i += 1

            result.append(word)

        return result
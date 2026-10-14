class Solution:

    # First naive solution
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if len(res) > 0:
                res += ","
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split(",")
        return res
class Solution:
    # Solution
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_string.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded_string

    # Own solution
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        count = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                c = int(count)
                word = ""
                for j in range(c):
                    word += s[i+1+j]
                decoded_string.append(word)
                i += c
                count = ""
            else:
                count+= s[i]
            i += 1
        return decoded_string

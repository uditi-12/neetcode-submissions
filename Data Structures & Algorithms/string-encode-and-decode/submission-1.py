class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":      # find the end of the length number
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])  # the string right after '#'
            i = j + 1 + length       # jump to the start of the next one
        return res

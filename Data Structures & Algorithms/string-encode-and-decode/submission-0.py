class Solution:

    def encode(self, strs: List[str]) -> str:
        # finding a way to encode it somehow
        res = ""
        for s in strs:
            # res(string) is composed of len of word s + # + actual word s (as one pair)
            res += str(len(s)) + "#" + s
        return res
        
    # the s is the res from encode
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
       
class Solution:

    def encode(self, strs: List[str]) -> str:
        self.length = []
        ans = ""
        for word in strs:
            self.length.append(len(word))
            ans += word
        return ans


    def decode(self, s: str) -> List[str]:
        begin = 0
        ans = []
        for l in self.length:
            if l == 0:
                ans.append("")
            else:
                ans.append(s[begin:begin+l])
                begin += l
        return ans
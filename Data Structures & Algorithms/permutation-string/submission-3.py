class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1arr = [0]*26
        s2arr = [0]*26
        lens1 = len(s1)
        lens2 = len(s2)
        if lens2 < lens1:
            return False
        for i in range(lens1):
            s1arr[ord(s1[i])-ord('a')] += 1
            s2arr[ord(s2[i])-ord('a')] += 1
        if self.checkArr(s1arr, s2arr):
            return True
        for i in range(lens1, lens2):
            s2arr[ord(s2[i-lens1])-ord('a')] -= 1
            s2arr[ord(s2[i])-ord('a')] += 1
            if self.checkArr(s1arr, s2arr):
                return True
        return False

    def checkArr(self, s1: str, s2: str) -> bool:
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True
            



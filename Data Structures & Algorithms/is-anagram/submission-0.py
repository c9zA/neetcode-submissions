from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct1 = Counter(s)
        ct2 = Counter(t)
        if len(ct1)!=len(ct2):
            return False
        for key, val in ct1.items():
            if ct2[key]!=val:
                return False
        return True
        
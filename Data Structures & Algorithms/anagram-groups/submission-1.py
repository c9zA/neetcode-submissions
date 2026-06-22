import numpy as np
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(lambda: [])
        for i in range(len(strs)):
            keyArr = [0]*26
            for ch in strs[i]:
                keyArr[ord(ch)-ord('a')] += 1
            key = tuple(keyArr)
            hmap[key].append(i)
        ans = []
        for arr in hmap.values():
            temp = []
            for idx in arr:
                temp.append(strs[idx])
            ans.append(temp)
        return ans

            
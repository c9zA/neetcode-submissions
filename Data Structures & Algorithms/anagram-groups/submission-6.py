class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(lambda: [])
        for word in strs:
            keyArr = [0]*26
            for ch in word:
                keyArr[ord(ch)-ord('a')] += 1
            key = tuple(keyArr)
            hmap[key].append(word)
        return list(hmap.values())
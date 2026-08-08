from math import ceil

class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(lambda: [])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        r = len(self.hmap[key])-1
        l = 0
        if not self.hmap[key] or timestamp<self.hmap[key][0][0]:
            return ""
        while r>l:
            m = ceil((r+l)/2)
            if self.hmap[key][m][0]>timestamp:
                r = m-1
            else:
                l = m
        return self.hmap[key][l][1] if l<len(self.hmap[key]) else self.hmap[key][-1][1]

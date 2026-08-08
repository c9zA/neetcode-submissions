class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(lambda: [])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        r = len(self.hmap[key])-1
        l = 0
        ans = ""
        while r>=l:
            m = (r+l)>>1
            if self.hmap[key][m][0]==timestamp:
                return self.hmap[key][m][1]
            elif self.hmap[key][m][0]<timestamp:
                ans = self.hmap[key][m][1]
                l = m+1
            else:
                r = m-1
        return ans
            
        

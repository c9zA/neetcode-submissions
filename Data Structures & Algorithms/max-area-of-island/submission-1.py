class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rct = len(grid)
        cct = len(grid[0])
        dir = [[1,0],[0,1],[-1,0], [0, -1]]
        def recurse(r,c, count):
            count +=1
            grid[r][c]=0
            for dr, dc in dir:
                nr = r+dr
                nc = c+dc
                if -1<nr<rct and -1<nc<cct and grid[nr][nc]==1:
                    count = recurse(nr, nc, count)
            return count
        for r in range(rct):
            for c in range(cct):
                if grid[r][c]==1:
                    ans = max(ans, recurse(r,c, 0))
        return ans
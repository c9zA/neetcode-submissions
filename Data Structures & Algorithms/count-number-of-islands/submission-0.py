class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        dir = [[0,1], [1, 0], [0, -1], [-1, 0]]
        rct = len(grid)
        cct = len(grid[0])
        def recurse(r, c):
            grid[r][c] = '0'
            for dr, dc in dir:
                nr = r+dr
                nc = c+dc
                if -1<nr<rct and -1<nc<cct and grid[nr][nc]=='1':
                    recurse(nr, nc)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    ans += 1
                    recurse(r, c)
        return ans
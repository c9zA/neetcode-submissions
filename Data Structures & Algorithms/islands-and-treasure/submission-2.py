class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rct = len(grid)
        cct = len(grid[0])
        dir = [[1,0],[-1,0],[0,-1],[0,1]]
        q = deque()
        for r in range(rct):
            for c in range(cct):
                if grid[r][c]==0:
                    q.append((r,c,0))
        while q:
            r, c, dist = q.popleft()
            dist+=1
            for dr, dc in dir:
                nr = r+dr
                nc = c+dc
                if -1<nr<rct and -1<nc<cct and grid[nr][nc]>dist:
                    grid[nr][nc]=dist
                    q.append((nr, nc, dist))
            
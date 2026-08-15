class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        print(board)
        colSet = set()
        sumSet = set()
        difSet = set()
        ans = []
        def recurse(r):
            if r==n:
                b = ["".join(board[i]) for i in range(n)]
                ans.append(b)
                return
            for c in range(n):
                if c in colSet or r-c in difSet or r+c in sumSet:
                    continue
                sumSet.add(r+c)
                colSet.add(c)
                difSet.add(r-c)
                board[r][c] = 'Q'
                recurse(r+1)
                board[r][c] = '.'
                difSet.remove(r-c)
                sumSet.remove(r+c)
                colSet.remove(c)
        recurse(0)
        return ans
            
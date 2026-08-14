class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    if self.recurse(r,c, 1, len(board), len(board[0]), word, board, set([(r,c)])):
                        return True
        return False
    
    def recurse(self, r, c, idx, lenr, lenc, word, board, hset):
        step = [(1,0), (-1,0), (0,1), (0, -1)]
        if idx==len(word):
            return True
        for dr, dc in step:
            if -1<r+dr<lenr and -1<c+dc<lenc and board[r+dr][c+dc]==word[idx] and (r+dr, c+dc) not in hset:
                hset.add((r+dr, c+dc))
                if self.recurse(r+dr, c+dc, idx+1, lenr, lenc, word, board, hset):
                    return True
                hset.remove((r+dr, c+dc))
        return False 
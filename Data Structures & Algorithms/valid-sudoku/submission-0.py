class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        alphabet = set()
        for i in range(9):
            alphabet.add(str(i+1))
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in alphabet or board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
        for j in range(9):
            rowSet = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in alphabet or board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
        for h in range(3):
            for i in range(3):
                subboardSet = set()
                for j in range(3):
                    for k in range(3):
                        if board[i*3+j][h*3+k]!='.':
                            if board[i*3+j][h*3+k] in subboardSet:
                                return False
                            subboardSet.add(board[i*3+j][h*3+k])
        return True
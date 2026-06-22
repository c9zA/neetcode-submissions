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
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
        seen = set()
        for i in range(81):
            if i%9 == 0:
                seen = set()
            if board[i//3%3+i//27*3][i%3+i//9*3%9]!='.' and board[i//3%3+i//27*3][i%3+i//9*3%9] in seen:
                return False
            seen.add(board[i//3%3+i//27*3][i%3+i//9*3%9])
        return True
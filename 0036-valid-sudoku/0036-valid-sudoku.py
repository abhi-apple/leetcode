class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        
        def issafe(i, j, val):
            for k in range(9):
                if (board[i][k] == val and k != j) or (board[k][j] == val and k != i) or (board[3*(i//3)+k//3][3*(j//3)+k%3] == val and (3*(i//3)+k//3 != i or 3*(j//3)+k%3 != j)):
                    return False
            return True
        
        for i in range(n):
            for j in range(m):
                if board[i][j]!='.':
                    
                    if not issafe(i, j, board[i][j]):

                        return False
        return True

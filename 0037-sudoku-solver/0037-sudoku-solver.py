class Solution:
    def solveSudoku(self, bo: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, c):
            for i in range(9):
                if board[i][col] == str(c):
                    return False
                if board[row][i] == str(c):
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == str(c):
                    return False
            return True
        def sud(bor):
            for i in range(len(bor)):
                for j in range(len(bor[0])):
                    if bor[i][j]=='.':
                        for c in range(1,10):
                            if isValid(bor,i,j,c):
                                bor[i][j]=str(c)
                                if sud(bor):
                                    return True
                                else:
                                    bor[i][j]='.'
                        return False
            return True
                                
        
        sud(bo)

#         def solveSudoku(board):
#             for i in range(len(board)):
#                 for j in range(len(board[0])):
#                     if board[i][j] == '.':
#                         for c in range(1,10):
#                             if isValid(board, i, j, c):
#                                 board[i][j] = str(c)
#                                 if solveSudoku(board):
#                                     return True
#                                 else:
#                                     board[i][j] = '.'
#                         return False
#             return True
#         solveSudoku(bo)

        
        
        
        
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

        def solveSudoku(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for c in range(1,10):
                            if isValid(board, i, j, c):
                                board[i][j] = str(c)
                                if solveSudoku(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        solveSudoku(bo)

        # def solve(bo):
        #     for i in range(len(bo)):
        #         for j in range(len(bo[0])):
        #             if bo[i][j]=='.':
        #                 for c in range(10):
        #                     if valid(bo,i,j,c):
        #                         bo[i][j]=str(c)
        #                         if solve(bo)==True:
        #                             return True
        #                         else:
        #                             bo[i][j]='.'
        #                 return False
        #     return True
        # def valid(bo,row,col,c):
        #     for i in range(10):
        #         if bo[i][col]==str(c) or bo[row][i]==str(c) or bo[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == str(c):
        #             return False
        #     return True
        
        
        
        
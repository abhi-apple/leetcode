class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe1( row, col, board, n):
            # check upper element
            duprow = row
            dupcol = col

            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            col = dupcol
            row = duprow
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            row = duprow
            col = dupcol
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            return True

        def solve( col, board, ans, n):
            if col == n:
                ans.append(board.copy())
                return
            for row in range(n):
                if isSafe1(row, col, board, n):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    solve(col + 1, board, ans, n)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

        ans = []
        board = ['.' * n for _ in range(n)]
        solve(0, board, ans, n)
        return ans
#         s=['*']*n
#         mat=[]
#         for i in range(n):
#             mat.append(s)
#         main=[]
#         print(mat)
        
#         def safe(row,col,mat,n):
#             print('in')
#             r=row
#             c=col
#             while row>=0 and col>=0:
#                 if mat[row][col]=='Q':
#                     return False
#                 row-=1
#                 col-=1
#             row=r
#             col=c
#             while col>=0:
#                 if mat[row][col]=='Q':
#                     return False
#                 col-=1
#             row=r
#             col=c
#             while row<=n and col>=0:
#                 if mat[row][col]=='Q':
#                     return False
#                 row+=1
#                 col-=1
#             return True
        
#         def f(col,mat,main,n):
#             print(col)
#             # print(mat)
#             if col==n:
#                 main.append(mat.copy())
#                 return
#             for row in range(n):
#                 if safe(row,col,mat,n):
#                     print('yes')
#                     print(row,col)
                    
#                     mat[row][col]='Q'
#                     print(mat[row][col])
#                     print(mat)
#                     f(col+1,mat,main,n)
#                     mat[row][col]='.'
            
#         f(0,mat,main,n)
#         return main


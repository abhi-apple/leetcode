class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        vis=set()
        cnt=0
        def dfs(i,j):
            vis.add((i,j))
            dire= [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for d in dire:
                ix,jx=i+d[0],j+d[1]
                if 0 <= ix < len(board) and 0 <= jx < len(board[0]) and (ix, jx) not in vis and board[ix][jx]==1:
                    dfs(ix,jx)
                    
        for i in range(len(board)):
            if i==0:
                for k in range(len(board[0])):
                    if board[0][k]==1:
                        dfs(0,k)
            if board[i][0]==1:
                dfs(i,0)
            if board[i][-1]==1:
                dfs(i,len(board[0])-1)
            if i==len(board)-1:
                for k in range(len(board[0])):
                    if board[i][k]==1:
                        dfs(i,k)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in vis and board[i][j]==1:
                    cnt+=1
        return cnt
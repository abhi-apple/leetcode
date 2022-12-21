class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans=0
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='X'):
                    if i==0 and j==0:
                        ans+=1
                    elif i==0:
                        if board[i][j-1]!='X':
                            ans+=1
                    elif j==0:
                        if board[i-1][j]!='X':
                            ans+=1
                    else:
                        if board[i][j-1]!='X' and board[i-1][j]!='X':
                            ans+=1
        return ans
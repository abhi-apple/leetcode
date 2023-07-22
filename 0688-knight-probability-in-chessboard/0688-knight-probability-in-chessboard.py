class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp={}

        def rec(i,j,nm):
            if i<0 or i>n-1 or j<0 or j>n-1 :
  
                return 0
            if nm==0:
                return 1
            if (i,j,nm) in dp:
                return dp[(i,j,nm)]
            
            dire = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
            now=0
            for d in dire:
                ix,jx=i+d[0],j+d[1]
                now+=rec(ix,jx,nm-1)
            dp[(i,j,nm)]=now
            return dp[(i,j,nm)]
        
        
        ans=rec(row,column,k)
        return ans/(8**k)
    
                
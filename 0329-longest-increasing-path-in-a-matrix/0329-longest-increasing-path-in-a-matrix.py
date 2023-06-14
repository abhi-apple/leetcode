class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        def rec(i,j):
            
            if i>len(matrix)-1 or j>len(matrix[0])-1 or i<0 or j<0:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            dire=[(-1,0),(0,-1),(1,0),(0,1)]
            maxi=0
            for d in dire:
                ix,jx,=i+d[0],j+d[1]
                if 0<=ix<len(matrix) and 0<=jx<len(matrix[0]) and matrix[ix][jx]>matrix[i][j]:
                    maxi=max(maxi,1+rec(ix,jx))
            dp[(i,j)]=maxi
            return dp[(i,j)]
        fin=0
        # fin=rec(0,0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                fin=max(fin,rec(i,j))
        return fin+1
                
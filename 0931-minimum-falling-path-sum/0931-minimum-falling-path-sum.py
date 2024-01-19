class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp={}
        n=len(matrix)
        mini=float('inf')
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==0 and 0<=j<n:
                return matrix[i][j]
            if 0>i or i>n-1 or 0>j or j>n-1:
                return float('inf')
            
            dp[(i,j)]=min(rec(i-1,j),rec(i-1,j-1),rec(i-1,j+1))+matrix[i][j]
            return dp[(i,j)]
        for i in range(n):
            mini=min(mini,rec(n-1,i))
        return mini
        
                
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        x=set()
        y=set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    x.add(i)
                    y.add(j)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i in x or j in y:
    
                    mat[i][j]=0
        
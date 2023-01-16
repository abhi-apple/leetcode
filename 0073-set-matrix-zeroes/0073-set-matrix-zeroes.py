class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        zi=set()
        zj=set()
                
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    zi.add(i)
                    zj.add(j)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i in zi or j in zj:
                    mat[i][j]=0
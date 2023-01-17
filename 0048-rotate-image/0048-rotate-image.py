class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(mat)):
            for j in range(i+1,len(mat[0])):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

        for i in range(len(mat)):
            mat[i].reverse()
            
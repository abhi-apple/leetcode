class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rc=[0]*m
        cc=[0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    rc[i]+=1
                    cc[j]+=1
        res=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and rc[i]==1 and cc[j]==1:
                    res+=1
        return res
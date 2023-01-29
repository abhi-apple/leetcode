class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        prev=[0]*n
        cur=[0]*n
        for i in range(n):
            prev[i]=mat[0][i]
        for i in range(1,n):
            for j in range(n):
                up=mat[i][j]+prev[j]
                ld=mat[i][j]
                if j-1>=0:
                    ld+=prev[j-1]
                else:
                    ld+=100000
                rd=mat[i][j]
                if j+1<n:
                    rd+=prev[j+1]
                else:
                    rd+=10000
                cur[j]=min(up,ld,rd)
            prev,cur=cur,prev
        return min(prev)
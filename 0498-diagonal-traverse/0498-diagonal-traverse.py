class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic={}
        n=len(mat)
        m=len(mat[0])
        dic={i:[] for i in range(n-1+m)}
        for i in range(n):
        
            for j in range(m):
                dic[i+j].append(mat[i][j])
        ans=[]
        for i in dic:
            if i & 1==0:
                dic[i]=dic[i][::-1]
            ans=ans+dic[i]
        return ans
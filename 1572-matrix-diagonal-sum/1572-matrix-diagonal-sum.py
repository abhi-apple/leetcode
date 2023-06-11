class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][i]
            ans+=mat[i][len(mat)-1-i]
        if len(mat)%2!=0:
            ans-=mat[len(mat)//2][len(mat)//2]
        return ans
class Solution:
    def generate(self, num: int) -> List[List[int]]:
        ans=[[1]*i for i in range(1,num+1)]
        for i in range(1,num):
            for j in range(1,i):
                ans[i][j]=ans[i-1][j]+ans[i-1][j-1]
        return ans
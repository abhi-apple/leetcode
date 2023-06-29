class NumMatrix:

    def __init__(self, ma: List[List[int]]):
        self.mat=ma
        self.pref=[]
        self.n=len(ma)
        self.m=len(ma[0])
        for i in range(self.n):
            now=[]
            sums=0
            for j in range(self.m):
                sums+=ma[i][j]
                now.append(sums)
            self.pref.append(now)

        
        
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            ans+=(self.pref[i][col2]-self.pref[i][col1])+(self.mat[i][col1])
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
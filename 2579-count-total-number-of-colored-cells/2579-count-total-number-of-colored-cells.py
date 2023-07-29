class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 5
        return (4*(n-1))+self.coloredCells(n-1)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        pr0=1
        pr1=1
        for i in range(2,n+1):
            cur=pr0+pr1
            pr1=pr0
            pr0=cur
        return pr0
class Solution:
    def tribonacci(self, n: int) -> int:
        pre0=0
        pre1=1
        pre2=1
        if n==0:
            return 0
        if n<3:
            return 1
        for i in range(3,n+1):
            cur=pre0+pre1+pre2
            pre0=pre1
            pre1=pre2
            pre2=cur
        return pre2
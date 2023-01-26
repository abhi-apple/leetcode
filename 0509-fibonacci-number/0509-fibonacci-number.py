class Solution:
    def fib(self, n: int) -> int:
        pr1=1
        pr2=0
        if n==0:
            return 0
        for i in range(2,n+1):
            cur=pr1+pr2
            pr2=pr1
            pr1=cur
        return pr1
        
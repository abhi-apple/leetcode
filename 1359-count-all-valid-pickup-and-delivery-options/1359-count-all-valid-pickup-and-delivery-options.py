class Solution:
    def countOrders(self, n: int) -> int:
        a = 1
        for i in range(2, n+1):
            a *= i*(2*i-1)
        return a % (10**9 + 7)
        
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp={}
        def rec(i):
            if i<2:
                return 0
            if i in dp:
                return dp[i]
            res=0
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                res=1+rec(i-1)
            dp[i]=res
            print(res)
            return res
        return sum(rec(i) for i in range(2, len(A)))

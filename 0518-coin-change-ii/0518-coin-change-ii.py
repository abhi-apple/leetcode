class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp = [[-1 for i in range(amount+1)] for j in range(n)]
            
        def res(ind,tar):
            if ind==0:
                if tar%coins[0]:
                    return 0
                else:
                    return 1
            if dp[ind][tar]!=-1:
                return dp[ind][tar]
            nt=res(ind-1,tar)
            tk=0
            if coins[ind]<=tar:
                tk=res(ind,tar-coins[ind])
            dp[ind][tar]=nt+tk
            return nt+tk
                
            
        return res(n-1,amount)
            
        
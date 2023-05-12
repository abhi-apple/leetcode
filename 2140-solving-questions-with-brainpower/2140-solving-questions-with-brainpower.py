class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def rec(ind):
            if ind>=len(questions):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            
            solv=questions[ind][0]+rec(ind+questions[ind][1]+1)
            ns=rec(ind+1)
            dp[ind]=max(solv,ns)
            return max(solv,ns)
        dp=[-1 for i in range(len(questions))]
        return rec(0)
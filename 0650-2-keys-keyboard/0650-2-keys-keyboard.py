class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        dp={}
        def rec(i,cp):
            if i==n:
                return 0
            
            if (i,cp) in dp:
                return dp[(i,cp)]
            if i>n:
                return float('inf')
            cop=rec(i*2,i)+2
            pst=float('inf')
            if cp:
                pst=rec(i+cp,cp)+1
            dp[(i,cp)]=min(cop,pst)
            return min(cop,pst)
        return rec(1,0)
            
# class Solution:
#     def minSteps(self, n: int) -> int:
#         if n == 1:
#             return 0
#         dp = {}

#         def rec(i, cp,did):
#             print(i,cp)
#             if i == n:
#                 return 0

#             if (i, cp,did) in dp:
#                 return dp[(i, cp,did)]
#             cop=float('inf')
#             if not did:
#                 cop = rec(i, i,True) + 1
#             pst = float('inf')
#             if i + cp <= n:
#                 pst = rec(i + cp, cp,False) + 1
            

#             dp[(i, cp,did)] = min(cop, pst)
#             return dp[(i, cp,did)]

#         return rec(1, 0,False)  

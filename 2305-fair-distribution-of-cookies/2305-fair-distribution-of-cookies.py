class Solution:
    def distributeCookies(self, cok: List[int], k: int) -> int:
        fin=float('inf')
        dp={}
        if len(cok)==k:
            return max(cok)
        def rec(arr,pats,cnt):
            nonlocal fin
            if cnt==k-1:
                pats[-1]=pats[-1]+sum(arr)
                fin=min(fin,max(pats))
                return 
            
            if (tuple(arr), tuple(pats),cnt) in dp:
                return dp[(tuple(arr),tuple(pats), cnt)]
            rec(arr,pats+[0],cnt+1)
            for i in range(len(arr)-1):
                pats[-1]=pats[-1]+arr[i]
                rec(arr[:i]+arr[i+1:],pats,cnt)
                pats[-1]=pats[-1]-arr[i]
                
            dp[(tuple(arr),tuple(pats), cnt)] = True
                
        rec(cok,[0],0)
        return fin

# from typing import List

# class Solution:
#     def distributeCookies(self, cok: List[int], k: int) -> int:
#         dp = {}
#         fin = float('inf')

#         def rec(arr, pats, cnt):
#             nonlocal fin
#             if cnt == k - 1:
#                 pats[-1] = pats[-1] + sum(arr)
#                 fin = min(fin, max(pats))
#                 return
#             if (tuple(arr), cnt) in dp:
#                 return dp[(tuple(arr), cnt)]
#             rec(arr, pats + [0], cnt + 1)
#             for i in range(len(arr) - 1):
#                 pats[-1] = pats[-1] + arr[i]
#                 rec(arr[:i] + arr[i+1:], pats, cnt)
#                 pats[-1] = pats[-1] - arr[i]
#             dp[(tuple(arr), cnt)] = True

#         rec(cok, [0], 0)
#         return fin

            
                
            
                
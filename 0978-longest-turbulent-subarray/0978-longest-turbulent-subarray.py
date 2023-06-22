class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        fin=0
        @cache
        def rec(i,inc,prev):
            if i==n:
                return 0
            maxi=0
            if prev==-1:
                maxi=rec(i+1,not inc,arr[i])+1
            elif not inc:
                if prev>arr[i]:
                    maxi=rec(i+1,not inc,arr[i])+1
            elif inc:
                if arr[i]>prev:
                    maxi=rec(i+1,not inc,arr[i])+1
            return maxi
        for i in range(n):
            fin=max(fin,rec(i,True,-1),rec(i,False,-1))
        return fin
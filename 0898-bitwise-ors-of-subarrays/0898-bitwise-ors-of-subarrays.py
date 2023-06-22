class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        fin=set()
        n=len(arr)
        dp={}
        def rec(i,ors):
            if (i,ors) in dp:
                return dp[(i,ors)]
            fin.add(ors)
            if i==n:
                return 
            
            rec(i+1,ors | arr[i])
            dp[(i,ors)]=None
            return 
        for i in range(n):
            rec(i,arr[i])
        return len(fin)
            
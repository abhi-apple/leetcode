class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=set()
        def rec(i,sums,arr):
            if i==k:
                if sums==n:
                    arr.sort()
                    if tuple(arr) not in ans:
                        ans.add(tuple(arr))
                return 
            for v in range(1,10):
                if v not in arr:
                    if sums+v<=n:
                        rec(i+1,sums+v,arr+[v])
            return 
        rec(0,0,[])
        return ans
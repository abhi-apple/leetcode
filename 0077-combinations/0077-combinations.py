class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def bk(st,cur):
            if len(cur)==k:
                res.append(cur.copy())
                return
            for i in range(st,n+1):
                cur.append(i)
                bk(i+1,cur)
                cur.pop()
        bk(1,[])
        return res
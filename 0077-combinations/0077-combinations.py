class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def bk(st,cur):
            if len(cur)==k:
                res.append(cur)
                return
            for i in range(st,n+1):
              
                bk(i+1,cur+[i])
               
        bk(1,[])
        return res
class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        dic={}
        def rec(r,c):
            if r==len(tr)-1:
                return tr[r][c]
            if (r,c) in dic:
                return dic[(r,c)]
            lft=rec(r+1,c)
            rgt=rec(r+1,c+1)
            dic[(r,c)]=min(lft,rgt)+tr[r][c]
            return min(lft,rgt)+tr[r][c]
        
        
        return rec(0,0)
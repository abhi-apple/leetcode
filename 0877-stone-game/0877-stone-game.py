class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp={}
        def rec(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            even=True if (r-l)%2 else False
            lft=piles[l] if even else 0
            rgt=piles[r] if even else 0
            dp[(l,r)]=max(rec(l+1,r)+lft,rec(l,r-1)+rgt)
            return dp[(l,r)]
        return rec(0,len(piles)-1)>sum(piles)//2
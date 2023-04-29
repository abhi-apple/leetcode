class Solution:
    def bagOfTokensScore(self, tok: List[int], po: int) -> int:
        tok.sort()
        l=0
        r=len(tok)-1
        sc=0
        maxi=0
        while l<=r:
            if po>=tok[l]:
        
                po-=tok[l]
                l+=1
                sc+=1
                maxi=max(maxi,sc)
                
            elif sc>0:
                po+=tok[r]
                r-=1
                sc-=1
            else:
                break
        return maxi
            
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        
        ans=Counter(s)
        for i in ans:
            if ans[i]%2!=0:
                k-=1
        if k<0:
            return False
        return True
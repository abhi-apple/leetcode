class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        par=[]
        def dfs(i):
            if i>=len(s):
                res.append(par.copy())
                return
            for j in range(i,len(s)):
                if self.ispa(s,i,j):
                    par.append(s[i:j+1])
                    dfs(j+1)
                    par.pop()
                    
        dfs(0)
        return res
    def ispa(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True
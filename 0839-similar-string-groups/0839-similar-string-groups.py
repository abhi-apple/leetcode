class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not strs:
            return 0
        
        visi=set()
        
        res=0
        def isim(p,q):
            cnt=0
            for i in range(len(p)):
                if p[i]!=q[i]:
                    cnt+=1
                if cnt>2:
                    return False
            if cnt==0 or cnt==2:
                return True
            
        def dfs(k):
            if k in visi:
                return 
            visi.add(k)
            for i in range(len(strs)):
                if isim(k,strs[i]):
                    dfs(strs[i])
                    
            
        for i in strs:
            if i not in visi:
                dfs(i)
                res+=1
        return res
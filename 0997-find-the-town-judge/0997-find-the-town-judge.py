class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans={}
        f=[]
        if n==1:
            return 1
        for i in range(len(trust)):
            a,b=trust[i]
            f.append(a)
            if b not in ans:
                ans[b]=1
            else:
                ans[b]+=1
                
        for i in ans:
            if ans[i]==n-1 and i not in f:
                return i
        return -1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans=[]
        fs=[]
        if n==1:
            return 1
        if len(trust)==1:
            return trust[0][1]
        for i in range(len(trust)):
            a,b=trust[i]
            fs.append(a)
            ans.append(b)
        
        for i in ans:
            if i not in fs and ans.count(i)==n-1:
                return i
        return -1
            
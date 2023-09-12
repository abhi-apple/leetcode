class Solution:
    def minDeletions(self, s: str) -> int:
        k=set(s)
        dic={}
        for i in k:
            dic[i]=s.count(i)
        dic=dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
        # for i in range(len(dic)):
        #     s.count()
        res=[]
        ans=0
        for i in dic.values():
            res.append(i)
        print(res)

        for i in range(len(res)):
            
            while res.count(res[i])!=1 and res[i]>0:
                # cnt=res.count(res[i])
                res[i]-=1
                ans=ans+1
                # print(ans,cnt)
                # cnt=cnt-1
        print(res)
        return ans
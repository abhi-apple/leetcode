class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        def find(w):
            l=[]
            m={}
            i=0
            for c in w:
                if c in m:
                    l.append(m[c])
                else:
                    i+=1
                    m[c]=i
                    l.append(m[c])
            return l
                    
        ans=[]
        mf=find(p)
        for i in words:
            ifi=find(i)
            if ifi==mf:
                ans.append(i)
        return ans
        # mt="0"
        # val={}
        # val[pattern[0]]=1
        # k=1
        # for i in pattern:
        #     if i not in val:
        #         mt+=str(k)
        #         k+=1
        #         val[i]=k
        #     elif len(pattern)>1:
        #         mt+=str(val[i])
        # print(mt)
        # fin=[]
        # for i in words:
        #     st="0"
        #     val={}
        #     val[i[0]]=1
        #     k=1
        #     for j in range(1,len(i)):
        #         if i[j] not in val:
        #             st+=str(k)
        #             k+=1
        #             val[i[j]]=k
        #         else:
        #             st+=str(val[i[j]])
        #     fin.append(st)
        # print(fin)
        # return [1,2]
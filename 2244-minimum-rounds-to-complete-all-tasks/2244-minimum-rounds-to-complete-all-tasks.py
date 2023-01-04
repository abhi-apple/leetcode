class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic={}
        for i in tasks:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        cnt=0
        
        for i in dic.values():
            if i==1:
                return -1
            elif i%3==0:
                cnt+=i//3
            elif i%3==1:
                cnt+=(i//3)+1
            elif i%3==2:
                cnt+=(i//3)+1
        return cnt
        
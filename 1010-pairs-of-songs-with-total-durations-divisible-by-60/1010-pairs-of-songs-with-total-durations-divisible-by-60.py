class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic={}
        cnt=0
        for i in time:
            newt=i%60
            if newt==0:
                if 0 in dic:
                    cnt+=dic[0]
            elif (60-newt) in dic:
                cnt+=dic[(60-newt)]
            if newt in dic:
                dic[newt]+=1
            else:
                dic[newt]=1
        return cnt
                
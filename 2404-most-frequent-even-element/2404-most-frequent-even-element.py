class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i%2==0:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        maxx=0
        op=-1
        for num,cnt in dic.items():
            if cnt>maxx:
                maxx,op=cnt,num
            elif cnt==maxx:
                op=min(op,num)
        return op
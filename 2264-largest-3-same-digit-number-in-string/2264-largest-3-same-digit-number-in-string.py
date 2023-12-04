class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=''
        for i in range(2,len(num)):
            if num[i]==num[i-1] and num[i-1]==num[i-2]:
                if ans=='':
                    ans=int(num[i]+num[i-1]+num[i-2])
                else:
                    ans=max(ans,int(num[i]+num[i-1]+num[i-2]))
        if ans==0:
            return '000'
        return str(ans)
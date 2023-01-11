class Solution:
    def findComplement(self, num: int) -> int:
        ans=bin(num)
        
        ans=ans[2:]
        l=list(ans)
        for i in range(len(ans)):
            if l[i]=='0':
                l[i]='1'
            else:
                l[i]='0'
        
        return int(''.join(l),2)
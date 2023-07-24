class Solution:
    def minFlips(self, s: str) -> int:
        comp1=''
        comp0=''
        var=0
        for i in s:
            comp1+=str(var^1)
            comp0+=str(var)
            var=var^1
        mini1=0
        mini0=0
        for i in range(len(s)):
            if s[i]!=comp1[i]:
                mini1+=1
            if s[i]!=comp0[i]:
                mini0+=1
        mini=min(mini1,mini0)
        
        for i in range(len(s)):
            if s[i]!=comp1[i]:
                mini1-=1
            if comp1[-1]=='1':
                comp1+='0'
            else:
                comp1+='1'
            if s[i]!=comp1[-1]:
                mini1+=1

                
            if s[i]!=comp0[i]:
                mini0-=1
            if comp0[-1]=='1':
                comp0+='0'
            else:
                comp0+='1'
            if s[i]!=comp0[-1]:
                mini0+=1
            # print(mini1,mini0)
            mini=min(mini,mini1,mini0)
        return mini
        
                
                
            
class Solution:
    def minSwaps(self, s: str) -> int:
        if abs(s.count('1')-s.count('0'))>1:
            return -1
        n=len(s)
        st1=''
        st0=''
        var=0
        for i in s:
            st0=st0+str(var)
            st1=st1+str(var^1)
            var=var^1
        ones=s.count('1')
        zer=s.count('0')
        mini=float('inf')
        if ones>zer:
            cnt=0
            i=0
            while i<n:
                if s[i]!=st1[i]:
                    cnt+=1
                i+=1
            mini=min(mini,cnt)
        elif zer>ones:
            cnt=0
            i=0
            while i<n:
                if s[i]!=st0[i]:
                    cnt+=1
                i+=1
            mini=min(mini,cnt)
        else:
            cnt=0
            i=0
            while i<n:
                if s[i]!=st0[i]:
                    cnt+=1
                i+=1
            mini=min(mini,cnt)
            cnt=0
            i=0
            while i<n:
                if s[i]!=st1[i]:
                    cnt+=1
                i+=1
            mini=min(mini,cnt)
            
            
                
        # print(st0,st1)
        return mini//2
        
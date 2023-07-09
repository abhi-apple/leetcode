class Solution:
    def largestVariance(self, s: str) -> int:
        res=0
        for ch1 in set(s):
            for ch2 in set(s):
                if ch1==ch2: continue
                ch2_front=False; has_ch2=False; var=0
                for i in range(len(s)):
                    if s[i]==ch1: var+=1
                    if s[i]==ch2:
                        has_ch2=True
                        var-=1
                        if ch2_front and var>=-1:
                            ch2_front=False
                            var+=1
                        elif var<0:
                            ch2_front=True
                            var=-1
                    res=max(res,var if has_ch2 else 0)
        return res 
        
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        p=set(s)
        print(p)
        cnt=s.count(s[0])
        lp=0
        for i in p:
            lp=s.count(i)
            if lp!=cnt:
                return False
        return True
            
        # for i in range(len(s)):
            
        # a=len(s)
        # s=set(s)
        # print(s)
        # print(a)
        # if len(s)==1:
        #     return True
        # if len(s)==a/2:
        #     return True
        # return False
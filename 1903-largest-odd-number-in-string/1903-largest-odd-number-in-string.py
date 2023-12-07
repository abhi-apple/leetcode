class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num:
            if int(num[-1]) &1==1:
                return num
            
            if len(num)==1:
                if int(num)&1==1:
                    return num
                return ""
            num=num[:-1]

        return num
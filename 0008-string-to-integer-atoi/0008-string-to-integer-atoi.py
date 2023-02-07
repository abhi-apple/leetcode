class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        sign = 1
        if str and str[0] in ('+', '-'):
            if str[0] == '-':
                sign = -1
            str = str[1:]
        ret = 0
        for c in str:
            if c.isdigit():
                ret = ret * 10 + int(c)
            else:
                break
        ret *= sign
        ret = min(ret, 2**31-1)
        ret = max(ret, -2**31)
        return ret


# class Solution:
#     def myAtoi(self, s: str) -> int:
#         p=list(s)
#         for i in range(len(p)):
#             if p[i]==' ':
#                 p.remove(i)
        
#         ans=''
#         si=False
#         if '-' in p and '+' in p:
#             return 0
#         if '-' in p and p[0]!='-':
#             return 0
#         for i in p:
#             if i.isalpha() or i=='.':
#                 break
#             if i=='-':
#                 si=True
#             if i.isdigit():
#                 ans=ans+i
#         if si:
#             if len(ans)>=10:
#                 return -2**31
#             elif ans=='':
#                 return 0
#             else:
#                 return -int(ans)
#         else:
#             if len(ans)>=10:
#                 return 2**31-1
#             elif ans=='':
#                 return 0
#             else:
#                 return int(ans)
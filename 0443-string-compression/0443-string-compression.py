# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         ans=''
#         ft=chars.copy()
#         ft.sort()
#         i=0
#         while i<len(ft):
#             cnt=ft.count(ft[i])
#             if cnt>1:
#                 ans=ans+ft[i]+str(cnt)
#                 i=i+cnt
#             else:
#                 ans=ans+ft[i]
#                 i+=1
#         chars=list(ans)
#         return len(ans)
            
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # pointer for current position in chars
        j = 0  # pointer for current position in output string
        
        while i < len(chars):
            # count the number of consecutive repeating characters
            count = 1
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            # write the character and its count to output string
            chars[j] = chars[i]  # write the character
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
            
            i += 1  # move to the next character
        
        return j

# class Solution:
#     def convertToTitle(self, col: int) -> str:
#         fin=''
#         mains='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
#         while col>0:
#             now=(col%26)
#             print(now)
#             if now!=0:
#                 fin=mains[(col%26)-1]+fin
  
                
#             col=col//26
#         return fin
class Solution:
    def convertToTitle(self, col: int) -> str:
        fin = ''
        mains = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        while col > 0:
        
            now = (col - 1) % 26  # Adjusted calculation for 0-based indexing

            fin = mains[now] + fin
            col = (col - 1) // 26  # Adjusted calculation for integer division
        
        return fin

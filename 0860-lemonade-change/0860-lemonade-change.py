# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         fiv=0
#         ten=0
#         for i in bills:
#             if i==5:
#                 fiv+=1
#             elif i==10:
#                 if fiv>1:
#                     fiv-=1
#                     ten+=1
#                 else:
#                     return False
#             elif i==20:
#                 if ten>=1 and fiv>=1:
#                     ten-=1
#                     fiv-=1
    
#                 elif fiv>=3 and ten<1:
#                     fiv-=3
        
#                 else:
#                     return False
#         return True
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        for b in bills:
            if b == 5:
                count5+=1
            elif b == 10:
                if count5 == 0:
                    return False
                count10+=1
                count5-=1
            else:
                if (count5>=1 and count10>=1):
                    count5-=1
                    count10-=1
                elif count5>=3:
                    count5-=3
                else:
                    return False
        return True

        
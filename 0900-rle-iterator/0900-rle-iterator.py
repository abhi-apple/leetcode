# class RLEIterator:

#     def __init__(self, encoding: List[int]):
#         self.dic={}
#         i=0
#         while i<len(encoding):
#             self.dic[encoding[i+1]]=encoding[i]
#             i+=2
#         # print(self.dic)

#     def next(self, n: int) -> int:
#         for i in self.dic:
#             if self.dic[i]>=n:
#                 self.dic[i]-=n
#                 return i
#             else:
#                 n=n-self.dic[i]
#                 self.dic[i]=0
                
                
#         return -1
from typing import List

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.current_pos = 0

    def next(self, n: int) -> int:
        while self.current_pos < len(self.encoding):
            count = self.encoding[self.current_pos]
            value = self.encoding[self.current_pos + 1]
            if count >= n:
                self.encoding[self.current_pos] -= n
                return value
            else:
                n -= count
                self.current_pos += 2
        return -1
        



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
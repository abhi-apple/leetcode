import heapq
class SummaryRanges:

    def __init__(self):
        self.lst=[]
        

    def addNum(self, val: int) -> None:
        heapq.heappush(self.lst,[val,val])
        

    def getIntervals(self) -> List[List[int]]:
        tmp=[]
        while self.lst:
            cur=heapq.heappop(self.lst)
            if tmp and cur[0]<=tmp[-1][1]+1:
                tmp[-1][1]=max(cur[1],tmp[-1][1])
            else:
                tmp.append(cur)
        self.lst=tmp
        return self.lst
                
                
                
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
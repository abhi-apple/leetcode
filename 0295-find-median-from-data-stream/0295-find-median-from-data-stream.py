class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        if self.small and self.large and -self.small[0]>self.large[0]:
            val=-(heapq.heappop(self.small))
            heapq.heappush(self.large,val)
        if len(self.small)>len(self.large)+1:
            val=-(heapq.heappop(self.small))
            heapq.heappush(self.large,val)
        if len(self.small)+1<len(self.large):
            val=-(heapq.heappop(self.large))
            heapq.heappush(self.small ,val)
            
            
        

    def findMedian(self) -> float:
        if len(self.large)==len(self.small):
            return (self.large[0]-self.small[0])/2
        elif len(self.large)>len(self.small):
            return float(self.large[0])
        else:
            return -float(self.small[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
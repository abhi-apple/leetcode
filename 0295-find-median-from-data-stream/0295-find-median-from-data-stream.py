class MedianFinder:

    def __init__(self):
        self.l=[]

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        if len(self.l) & 1==1:
            return float(self.l[len(self.l)//2])
        else:
            n=len(self.l)//2
            return float((self.l[n]+self.l[n-1])/2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
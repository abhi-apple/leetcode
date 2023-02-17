class MyCircularQueue:

    def __init__(self, k: int):
        self.ls=list()
        self.k=k
        self.sz=0

    def enQueue(self, value: int) -> bool:
        if self.sz<self.k:
            self.ls.append(value)
            self.sz+=1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.sz>0:
            self.ls.pop(0)
            self.sz-=1
            return True
        return False
    
        

    def Front(self) -> int:
        if self.sz>0:
            return self.ls[0]
        return -1
        

    def Rear(self) -> int:
        if self.sz>0:
            return self.ls[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if self.sz==0:
            return True
        return False
    
        

    def isFull(self) -> bool:
        if self.sz==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class MyQueue:

    def __init__(self):
        self.enq=[]

    def push(self, x: int) -> None:
        self.enq.append(x)

    def pop(self) -> int:
        return self.enq.pop(0)

    def peek(self) -> int:
        ans=self.enq.pop(0)
        res=[ans]
        print(res)
        self.enq=res + self.enq
        return ans

    def empty(self) -> bool:
        if len(self.enq)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
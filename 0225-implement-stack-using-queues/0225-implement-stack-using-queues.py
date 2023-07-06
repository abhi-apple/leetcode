class MyStack:

    def __init__(self):
        self.que=deque()
        
        

    def push(self, x: int) -> None:
        self.que.append(x)
        
        

    def pop(self) -> int:
        n=len(self.que)
        for i in range(n):
            k=self.que.popleft()
            if i!=n-1:
                self.que.append(k)
        return k
        

    def top(self) -> int:
        return self.que[-1]
        

    def empty(self) -> bool:
   
        if len(self.que):
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
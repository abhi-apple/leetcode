class StockSpanner:

    def __init__(self):
        self.stack = []  # Use a stack to store the indices of the elements
        self.lis = []

    def next(self, price: int) -> int:
        self.lis.append(price)
        while self.stack and self.lis[self.stack[-1]] <= price:
            self.stack.pop()
        if not self.stack:
            cnt = len(self.lis)
        else:
            cnt = len(self.lis) - self.stack[-1] - 1
        self.stack.append(len(self.lis) - 1)
        return cnt

        # self.lis.append(price)
        # cnt = 0  # Initialize cnt to 1 to count the current price
        # i = len(self.lis) - 1  # Start from the end of the list
        # while i >= 0 and self.lis[i] <= price:
        #     cnt += 1
        #     i -= 1
        # return cnt
    # def next(self, price: int) -> int:
    #     self.lis.append(price)
    #     i=1
    #     cnt=0
    #     while i<=len(self.lis):
    #         print(self.lis)
    #         print(price,self.lis[-i])
    #         if price<=self.lis[-i]:
    #             i+=1
    #             cnt+=1
    #             print(cnt,i)
    #         else:
    #             break
    #     return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
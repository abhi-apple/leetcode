class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur=homepage
        self.prev=[]
        self.fo=[]
        

    def visit(self, url: str) -> None:
        self.prev.append(self.cur)
        self.cur=url
        self.fo=[]
        
        

    def back(self, steps: int) -> str:
        le=min(steps,len(self.prev))
        while le:
            self.fo.append(self.cur)
            self.cur=self.prev.pop()
            le-=1
        return self.cur
        

    def forward(self, steps: int) -> str:
        le=min(steps,len(self.fo))
        while le:
            self.prev.append(self.cur)
            self.cur=self.fo.pop()
            le-=1
        return self.cur
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class FreqStack:

    def __init__(self):
        self.dic = {}
        self.stack = []
        self.cnt = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.cnt and self.cnt[val]>0:
            # print(self.dic,self.cnt,val)
            self.dic[self.cnt[val]].remove(val)
            self.cnt[val] += 1
            if self.cnt[val] in self.dic:
                self.dic[self.cnt[val]].append(val)
            else:
                self.dic[self.cnt[val]] = [val]
        else:
            self.cnt[val] = 1
            if 1 in self.dic:
                self.dic[1].append(val)
            else:
                self.dic[1] = [val]

    def pop(self) -> int:
        n = len(self.stack) - 1
        i = max(self.dic.keys())
        while n >= 0:
       
            if self.stack[n] in self.dic[i]:
             
                val = self.stack.pop(n)
                self.cnt[val] -= 1
                self.dic[i].remove(val)
                if len(self.dic[i])==0:
                    del self.dic[i]
                if self.cnt[val] > 0:
                    if self.cnt[val] in self.dic:
                        self.dic[self.cnt[val]].append(val)
                    else:
                        self.dic[self.cnt[val]] = [val]
                break
            n -= 1

        return val


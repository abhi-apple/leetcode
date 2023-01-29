class LFUCache:

    def __init__(self, capacity: int):
        self.cache=dict()
        self.min_freq=1
        self.freq=dict()
        self.hash=dict()
        self.size=capacity

    def get(self, key: int) -> int:
        if key in self.hash:
            self.cache[self.freq[key]].remove(key)
            self.freq[key]+=1
            try:
                self.cache[self.freq[key]].append(key)
            except:
                self.cache[self.freq[key]]=list()
                self.cache[self.freq[key]].append(key)
            return self.hash[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.cache[self.freq[key]].remove(key)
            self.freq[key]+=1
            try:
                self.cache[self.freq[key]].append(key)
            except:
                self.cache[self.freq[key]]=list()
                self.cache[self.freq[key]].append(key)
            self.hash[key]=value
        elif len(self.hash)<self.size:
            try:
                self.cache[self.min_freq].append(key)
            except:
                self.cache[self.min_freq]=list()
                self.cache[self.min_freq].append(key)
            self.hash[key]=value
            self.freq[key]=1
        else:
            if self.size==0:
                return
            while len(self.cache[self.min_freq])==0:
                self.min_freq+=1
            lru=self.cache[self.min_freq][0]
            self.hash.pop(lru)
            self.freq.pop(lru)
            del self.cache[self.min_freq][0]
            self.min_freq=1
            self.put(key,value)
            return

            
                    
            
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
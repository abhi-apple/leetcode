
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:

            self.dic[key]=self.dic.pop(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            
            if len(self.dic)==self.size:
                self.dic.popitem(last=False)
              
        else:
            self.dic.pop(key)
        self.dic[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
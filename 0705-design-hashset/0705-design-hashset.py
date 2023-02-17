class MyHashSet:

    def __init__(self):
        self.dic=list()
        

    def add(self, key: int) -> None:
        if key not in self.dic:
            self.dic.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic.remove(key)
        
        

    def contains(self, key: int) -> bool:
        if key in self.dic:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
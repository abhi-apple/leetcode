class MyHashMap:

    def __init__(self):
        self.res=[]

    def put(self, key: int, value: int) -> None:
        isn=False
        for i in range(len(self.res)):
            if self.res[i][0]==key:
                isn=True
                self.res[i][1]=value
                return
        if not isn:
            self.res.append([key,value])
            return 
            
            
        

    def get(self, key: int) -> int:
        for i in range(len(self.res)):
            if self.res[i][0]==key:
                return self.res[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.res)):
            if self.res[i][0]==key:
                self.res[i][0]=-1
                return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
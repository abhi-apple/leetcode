class Allocator:

    def __init__(self, n: int):
        self.arr=['#']*n
        self.sz=n
        

    def allocate(self, size: int, mID: int) -> int:
        i=0

        while i<self.sz:
            j=i
            while j<self.sz and self.arr[j]=='#':
                j+=1
                if j-i>=size:
                    break
                
            if j-i>=size:
                for k in range(i,i+size):
                    self.arr[k]=mID
                return i
            i=j+1
        return -1
                
                
            
        

    def free(self, mID: int) -> int:
        cnt=0
        for i in range(self.sz):
            if self.arr[i]==mID:
                self.arr[i]='#'
                cnt+=1
        return cnt
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
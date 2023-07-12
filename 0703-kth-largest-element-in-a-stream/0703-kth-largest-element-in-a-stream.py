class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth=k
        self.arr=nums
        heapq.heapify(self.arr)
        while len(self.arr)>k:
            heapq.heappop(self.arr)
        

    def add(self, val: int) -> int:
        
        if not self.arr:
            heapq.heappush(self.arr,val)
        elif val>self.arr[0] or len(self.arr)<self.kth:
            heapq.heappush(self.arr,val)
            if len(self.arr)>self.kth:
                heapq.heappop(self.arr)
        return self.arr[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
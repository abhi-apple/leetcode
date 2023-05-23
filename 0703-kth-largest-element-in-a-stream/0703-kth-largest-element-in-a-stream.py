class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth=k
        self.arr=nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort(reverse=True)
        return self.arr[self.kth-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
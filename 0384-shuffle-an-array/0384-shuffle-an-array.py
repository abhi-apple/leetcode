class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.real=nums[:]
        # self.original = nums
        # self.nums = nums
    def reset(self) -> List[int]:
        return self.real

    def shuffle(self) -> List[int]:
        ans = self.arr
        # ans.append(ans.pop(ans.index(ans[0])))
        
        for i in range(len(ans)):
            a=random.randint(0,len(ans)-1)
            b=random.randint(0,len(ans)-1)
            ans[a],ans[b]=ans[b],ans[a]
        # print(self.nums,"shu")
        # print(self.original,"ress")
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
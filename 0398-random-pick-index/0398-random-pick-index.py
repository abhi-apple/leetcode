import random
class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for idx, num in enumerate(nums):
            self.d[num].append(idx)

    def pick(self, tar: int) -> int:
        return random.choice(self.d[tar])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
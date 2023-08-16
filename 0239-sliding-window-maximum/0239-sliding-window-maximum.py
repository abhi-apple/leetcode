class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que=deque()
        ans=[]
        n=len(nums)
        for i in range(n):
            if que and que[0]==i-k:
                que.popleft()
            while que and nums[que[-1]]<nums[i]:
                que.pop()
            que.append(i)
            if i>=k-1:
                ans.append(nums[que[0]])
        return ans
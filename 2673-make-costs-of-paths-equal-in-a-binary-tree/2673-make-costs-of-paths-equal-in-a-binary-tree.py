class Solution:
    def minIncrements(self, n: int, nums: List[int]) -> int:
        ans=0
        def bfs(node):
            nonlocal ans
            if node>n:
                return 0
            lft=bfs(node*2)
            rgt=bfs(node*2 +1)
            ans+=abs(lft-rgt)
            return nums[node-1]+max(lft,rgt)
        bfs(1)
        return ans
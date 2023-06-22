class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        sums=sum(nums)
        if sums%4!=0:
            return False
        n = len(nums)
        nums.sort(reverse=True)
        k=4
        target = int(sums / k)
        used = [False] * n

        def dfs(index, total, k): 

            if k == 0:
                return True

            if total == 0:
                return dfs(0, target, k - 1)

            for i in range(index, n):

                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue

                if used[i] or total - nums[i] < 0:
                    continue

                used[i] = True
                if dfs(i + 1, total - nums[i], k):
                    return True
                used[i] = False
            return False

        return dfs(0, target, k)
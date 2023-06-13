class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        fin=[]
        cnt=Counter(nums)
        def dfs(arr):
            nonlocal fin
            if len(arr)==len(nums):
                fin.append(arr)
                return 
            for n in cnt:
                if cnt[n]>0:
                    cnt[n]-=1
                    dfs(arr+[n])
                    cnt[n]+=1
        dfs([])
        return fin
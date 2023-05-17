class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            sums=0
            for j in str(nums[i]):
                sums+=int(j)
            ans.append(sums)
        maxi=-1
        print(ans)
        dic={}
        for i in range(len(ans)):
            if ans[i] in dic:
                dic[ans[i]].append(i)
            else:
                dic[ans[i]]=[]
                dic[ans[i]].append(i)
        for i in dic:
            if len(dic[i])>1:
                print(nums[dic[i][0]],nums[dic[i][1]])
                maxi=max(maxi,nums[dic[i][-1]]+nums[dic[i][-2]])
        return maxi
    
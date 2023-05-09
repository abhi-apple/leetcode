class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[]
        dic={}
        zc=[0]
        oc=[0]
        cntz=0
        cnto=0
        for i in range(len(nums)):
            if nums[i]==0:
                cntz+=1
            zc.append(cntz)
        rev=nums[::-1]
        for i in range(len(nums)):
            if rev[i]==1:
                cnto+=1
            oc.append(cnto)
        oc=oc[::-1]
        for i in range(len(nums)+1):
            sums=zc[i]+oc[i]
            ans.append(sums)
            if sums in dic:
                dic[sums].append(i)
            else:
                dic[sums]=[]
                dic[sums].append(i)

        ans.sort()
        return dic[ans[-1]]

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        pref=[]
        suf=[]
        n=len(nums)
        mini=0
        ind=0
        for i in range(n):
            if nums[i]>mini:
                pref.append(i)
                ind=i
                mini=nums[i]
            else:
                pref.append(ind)
        # print(pref)
        maxi=float('inf')
        for i in range(n-1,-1,-1):
            if nums[i]<maxi:
                suf.append(i)
                ind=i
                maxi=nums[i]
            else:
                suf.append(ind)
        suf=suf[::-1]
        # print(suf)
        cnt=0
        # print(suf)
        # print(pref)
        # def forall(ind):
        #     return True
        for i in range(1,n-1):
            if suf[i]==pref[i]:
                cnt+=2
            elif nums[i-1]<nums[i] and nums[i]<nums[i+1]:
                cnt+=1
        return cnt
            
                
            
            
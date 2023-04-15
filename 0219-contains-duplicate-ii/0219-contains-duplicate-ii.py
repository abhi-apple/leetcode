class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        dif=10000
        for i in dic.values():
            if len(i)==1:
                continue
            for j in range(1,len(i)):
                dif=min(dif,abs(i[j]-i[j-1]))
            if dif<=k:
                return True
        return False
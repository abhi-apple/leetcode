class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        fr={}
        for i in nums:
            if i in fr:
                fr[i]+=1
            else:
                fr[i]=1
        for i in nums:
            if fr[i]%2!=0:
                return False
        return True
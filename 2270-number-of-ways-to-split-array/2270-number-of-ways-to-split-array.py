class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefl=[]
        prefr=[]
        sums=0
        for i in nums:
            sums+=i
            prefl.append(sums)
        sums=0
        for i in nums[::-1]:
            sums+=i
            prefr.append(sums)
        prefr=prefr[::-1]
        # print(prefl,prefr)
        prefl.pop()
        prefr=prefr[1:]
        cnt=0
        for i in range(len(prefl)):
            if prefl[i]-prefr[i]>=0:
                cnt+=1
                
        return cnt
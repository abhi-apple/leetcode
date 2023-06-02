class Solution:
    def twoSum(self, num: List[int], tar: int) -> List[int]:
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j]==tar:
                return [i+1,j+1]
            elif num[i]+num[j]>tar:
                j-=1
            else:
                i+=1
                
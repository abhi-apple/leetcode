class Solution:
    def kidsWithCandies(self, can: List[int], ex: int) -> List[bool]:
        maxi=max(can)
        ans=[]
        for i in range(len(can)):
            if can[i]+ex>=maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans
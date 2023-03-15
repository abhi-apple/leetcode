class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st=[i for i in range(1,len(nums)+1)]
        return set(set(st)-set(nums))
                
                
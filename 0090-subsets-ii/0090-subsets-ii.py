
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        st=[]
        
        nums.sort()
        def rec(i,arr):
            if i==len(nums):
                if arr not in st:
                    st.append(arr)
                return 
            rec(i+1,arr)
            rec(i+1,arr+[nums[i]])
        rec(0,[])
        return st
            
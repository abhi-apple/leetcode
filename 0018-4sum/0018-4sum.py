class Solution:
    def fourSum(self, nums: List[int], tar: int) -> List[List[int]]:
        st=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    x=tar-(nums[i]+nums[k]+nums[j])
                    if x in nums[k+1:]:
                        res=[]
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[k])
                        res.append(x)
                        res.sort()
                        if res not in st:
                            st.append(res)
        return st
                        
                    
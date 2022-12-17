class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums,reverse=1),key=nums.count)
        # st={}
        # for i in nums:
        #     if i in st:
        #         st[i]+=1
        #     else:
        #         st[i]=1
        # print(st)
        # for i,j in st.items():
        #     print(i,j)
        # # for i,s in enumerate(nums):
        # #     if 
        # #     print(i,s)
        # return [0,1]
    
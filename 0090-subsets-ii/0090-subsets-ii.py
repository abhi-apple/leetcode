# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans=set()
#         def subs(i,ls):
#             if i==len(nums):
#                 ls.sort()
#                 ans.add(tuple(ls))
#                 return 
#             ls.append(nums[i])
#             subs(i+1,ls)
#             ls.pop()
#             subs(i+1,ls)
#         subs(0,[])
#         return ans
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(start, path):
            ans.add(tuple(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        nums.sort()
        backtrack(0, [])
        return ans

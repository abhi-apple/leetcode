class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            val = -nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if nums[k] + nums[j] == val:
                    if [nums[i], nums[k], nums[j]] not in ans:
                        ans.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                elif nums[k] + nums[j] > val:
                    j -= 1
                else:
                    k += 1
        return ans

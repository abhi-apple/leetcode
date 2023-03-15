class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums=defaultdict(int)
        res=0
        for i in nums1:
            for j in nums2:
                nums[i+j]+=1
        for k in nums3:
            for l in nums4:
                res+=nums[-(k+l)]
        return res
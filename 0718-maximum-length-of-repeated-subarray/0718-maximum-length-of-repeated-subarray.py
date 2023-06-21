class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[-1 for i in range(len(nums2))] for j in range(len(nums1))]
        def rec(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=0
            if nums1[i]==nums2[j]:
                maxi=max(maxi,rec(i-1,j-1)+1)
            dp[i][j]=maxi
            return dp[i][j]
        main=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                main=max(main,rec(i,j))
        return main
            
            
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=[(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs=sorted(pairs,key=lambda p:p[1],reverse=True)
        minh=[]
        n1s=0
        res=0
        for n1,n2 in pairs:
            n1s+=n1
            heapq.heappush(minh,n1)
            if len(minh)>k:
                n1pop=heapq.heappop(minh)
                n1s-=n1pop
            if len(minh)==k:
                res=max(res,n1s*n2)
        return res
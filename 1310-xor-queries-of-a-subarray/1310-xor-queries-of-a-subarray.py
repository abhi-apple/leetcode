class Solution:
    def xorQueries(self, arr: List[int], que: List[List[int]]) -> List[int]:
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1] ^ i)
        ans = []
        for l,q in que:
            ans.append(prefix[q+1] ^ prefix[l])
        return ans
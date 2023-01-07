class Solution:
    def minFlips(self, target: str) -> int:
        prev='0'
        ans=0
        for i in target:
            if i !=prev:
                ans+=1
                prev=i
        return ans
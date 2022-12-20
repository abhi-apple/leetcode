class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=s.split(' ')
        res=res[0:k]
        ans=' '.join(res)
        return ans
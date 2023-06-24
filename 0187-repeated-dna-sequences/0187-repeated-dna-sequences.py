class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        seen,dic=set(),set()
        for i in range(n-9):
            cur=s[i:i+10]
            if cur in seen:
                dic.add(cur)
            seen.add(cur)
        return dic
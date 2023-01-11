class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=['']
        for i in s:
            if i.isdigit():
                ans=[x+i for x in ans]
            else:
                ans= [c+i.lower() for c in ans] + [c+i.upper() for c in ans]
        return ans
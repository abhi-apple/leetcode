class Solution:
    def closetTarget(self, words: List[str], target: str, st: int) -> int:
        if target not in words:
            return -1
        n=len(words)
        finp=float("inf")
        for i in range(n):
            if words[i]==target:
                finp=min(finp,abs(i-st),n-abs(i-st))
        return finp

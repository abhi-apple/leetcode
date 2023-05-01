class Solution:
    def average(self, sa: List[int]) -> float:
        sa.sort()
        sa=sa[1:-1]
        return sum(sa)/len(sa)
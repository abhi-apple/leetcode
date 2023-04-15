class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if i+1 > c:
                return i
        return n

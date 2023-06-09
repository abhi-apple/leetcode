class Solution:
    def nextGreatestLetter(self, lett: List[str], tar: str) -> str:
        for i in range(len(lett)):
            if lett[i]>tar:
                return lett[i]
        return lett[0]
                
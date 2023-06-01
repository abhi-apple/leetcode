class Solution:
    def twoSum(self, main: List[int], tar: int) -> List[int]:
        for i in range(len(main)):
            if tar-main[i] in main and main.index(tar-main[i])!=i :
                return [i,main.index(tar-main[i])]
        return
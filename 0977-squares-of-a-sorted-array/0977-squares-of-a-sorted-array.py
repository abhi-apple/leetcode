class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        fin = []

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                fin.append(nums[i] ** 2)
                i += 1
            else:
                fin.append(nums[j] ** 2)
                j -= 1


        return fin[::-1]

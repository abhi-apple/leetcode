class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for s in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(len(potions) - left)
        return res

            
                
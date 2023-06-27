class Solution:
    def shipWithinDays(self, w: List[int], da: int) -> int:
        i = max(w)
        j = sum(w)

        def rec(val):
            days = 1
            total = 0
            for weight in w:
                total += weight
                if total > val:
                    days += 1
                    total = weight
            return days

        fin = 0
        while i <= j:
            mid = (i + j) // 2
            if rec(mid) <= da:
                fin = mid
                j = mid - 1
            else:
                i = mid + 1
        return fin

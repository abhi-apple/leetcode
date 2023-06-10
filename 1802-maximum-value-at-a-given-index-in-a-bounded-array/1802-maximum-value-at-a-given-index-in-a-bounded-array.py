class Solution:
    def maxValue(self, n: int, index: int, maxi: int) -> int:
        l = 1
        h = maxi
        emr = n - index - 1
        eml = index
        res = -1
        
        while l <= h:
            mid = (l + h) // 2
            lefts = 0
            rgts = 0
            el = mid - 1
            
            if emr <= el:
                rgts = (el * (el + 1)) // 2 - ((el - emr) * (el - emr + 1)) // 2
            else:
                rgts = (el * (el + 1) // 2) + (emr - el)
            
            if eml <= el:
                lefts = (el * (el + 1)) // 2 - ((el - eml) * (el - eml + 1)) // 2
            else:
                lefts = (el * (el + 1) // 2) + (eml - el)
            
            sums = lefts + mid + rgts
            
            if sums <= maxi:
                l = mid + 1
                res = mid
            else:
                h = mid - 1
        
        return res

            
            
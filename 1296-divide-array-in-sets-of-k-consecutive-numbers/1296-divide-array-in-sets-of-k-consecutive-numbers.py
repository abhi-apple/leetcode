from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        cnt = Counter(nums)
        ans = sorted(cnt)
        
        while ans:
            start = ans[0]
            for i in range(start, start + k):
                if cnt[i] == 0:
                    return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    ans.remove(i)
        
        return True
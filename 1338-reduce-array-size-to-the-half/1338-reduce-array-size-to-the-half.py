class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)      
        freq = sorted(cnt.values(), reverse=True)
        
        half_size = len(arr) // 2
        ans = 0
        
        while half_size > 0:
            half_size -= freq[ans]
            ans += 1
        
        return ans
            
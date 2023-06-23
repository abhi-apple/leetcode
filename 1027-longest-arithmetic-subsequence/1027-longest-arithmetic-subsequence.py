from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)
        dp = [defaultdict(int) for _ in range(length)]
        max_value = 1
        
        for i in range(length):
            current_element = A[i]
            current_map = dp[i]
            
            for j in range(i):
                difference = current_element - A[j]
                prev_map = dp[j]
                new_value = prev_map.get(difference, 0) + 1
                current_map[difference] = new_value
                dp[i] = current_map
                max_value = max(max_value, current_map[difference])
        
        return max_value + 1

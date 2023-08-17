from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque()
        for i in range(1, 10):
            queue.append(str(i))
        
        result = []
        while queue:
            curr_str = queue.popleft()
            curr_num = int(curr_str)
            if curr_num <= high:
                if curr_num >= low:
                    result.append(curr_num)
                last_digit = int(curr_str[-1])
                if last_digit < 9:
                    queue.append(curr_str + str(last_digit + 1))
        
        return result

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

            
            
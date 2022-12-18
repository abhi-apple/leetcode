class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)
        # Iterate through the temperatures
        for i, t in enumerate(temperatures):
            # Pop the top element from the stack if it is smaller than the current temperature
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                # Calculate the waiting days and update the result array
                result[j] = i - j
            # Push the current index to the stack
            stack.append(i)
        return result
#         res=[]
    
#         for i in range(len(temperatures)):
#             ad=False
#             for j in range(i,len(temperatures)):
#                 if temperatures[j] >temperatures[i]:
#                     ad=True
#                     res.append(j-i)
#                     break
#             if ad==False:
#                 res.append(0)
#         return res
                
            
            
            
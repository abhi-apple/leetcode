from typing import List

class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        def rec(lft):
            if lft.isnumeric():
                return [int(lft)]
            
            res = []
            for i in range(len(lft)):
                if lft[i] in '+-*':
                    nowl = rec(lft[:i])
                    nowr = rec(lft[i + 1:])
                    
                    for lf in nowl:
                        for rg in nowr:
                            if lft[i] == '+':
                                res.append(lf + rg)
                            elif lft[i] == '-':
                                res.append(lf - rg)
                            else:
                                res.append(lf * rg)
                                
            return res
        
        return rec(exp)

# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:
#         #base case: if it's a number, return it
#         if expression.isnumeric():
#             return [int(expression)]
        
#         #general case
#         res = []
#         for i, char in enumerate(expression):
#             if char in ['+', '-', '*']:
#                 left = self.diffWaysToCompute(expression[:i])
#                 right = self.diffWaysToCompute(expression[i+1:])
#                 print(left,right)
#                 for le in left:
#                     for ri in right:
#                         if char == '+':
#                             res.append(le + ri)
#                         elif char == '-':
#                             res.append(le - ri)
#                         else: # char == '*'
#                             res.append(le * ri)
#         return res
            
            
            

            
            
            
#     def diffWaysToCompute(self, input):
#         return self.helper(input, {})

#     def helper(self, input, seen):
#         if input in seen:
#             return seen[input]
#         if input.isnumeric():
#             return [int(input)]
#         res = []
#         for i, c in enumerate(input):
#             if c in "+-*":
#                 res += [l+r if c == "+" else l-r if c == "-" else l*r 
#                             for l in self.helper(input[:i], seen) 
#                             for r in self.helper(input[i+1:], seen)]
#         seen[input] = res
#         return res
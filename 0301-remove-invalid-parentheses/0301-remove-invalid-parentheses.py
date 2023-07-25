# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         st=[]
#         for i in s:
#             if i=='(':
#                 st.append(i)
#             elif i==')':
#                 if st and  st[-1]=='(':
#                     st.pop()
#                 else:
#                     st.append(i)
 
#         if not st:
#             return [s]
        
#         op=st.count('(')
#         cl=st.count(')')
#         final=set()
#         def rec(par,opp,clp):
            
#             def safe(test):
#                 st=[]
#                 for i in test:
#                     if i=='(':
#                         st.append(i)
#                     elif i==')':
#                         if st and st[-1]=='(':
#                             st.pop()
#                         else:
#                             st.append(i)
#                 if '(' in st or ')' in st :
#                     return False
#                 return True
                
#             if opp==0 and clp==0 or not par:
          
#                 if safe(par):
#                     final.add(par)
#                 return 
#             if opp:
#                 for i in range(len(par)):
#                     if par[i]=='(':
#                         rec(par[:i]+par[i+1:],opp-1,clp)
#             if clp:
#                 for i in range(len(par)):
#                     if par[i]==')':
#                         rec(par[:i]+par[i+1:],opp,clp-1)
#             return 
                    
#         rec(s,op,cl)
#         return final

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(parentheses):
            count = 0
            for char in parentheses:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # Initialize the BFS queue with the input string
        queue = {s}
        found = False
        result = set()

        while queue:
            next_queue = set()
            for parentheses in queue:
                if is_valid(parentheses):
                    found = True
                    result.add(parentheses)
                if found:
                    continue
                # Generate all possible combinations by removing one character at a time
                for i in range(len(parentheses)):
                    if parentheses[i] in ('(', ')'):
                        next_queue.add(parentheses[:i] + parentheses[i + 1:])
            queue = next_queue

        return list(result)

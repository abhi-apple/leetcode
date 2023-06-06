class Solution:
    def checkValidString(self, s: str) -> bool:
        s = list(s)
        stack = []
        star_stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while stack and star_stack:
            if stack[-1] > star_stack[-1]:
                return False
            stack.pop()
            star_stack.pop()
        
        return len(stack) == 0


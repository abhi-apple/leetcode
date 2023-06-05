import math

class Solution:
    def evalRPN(self, tok: List[str]) -> int:
        st = []
        var = ['+', '-', '*', '/']
        
        for i in tok:
            if i in var:
                fir = int(st.pop())
                sec = int(st.pop())
                
                if i == '+':
                    ans = sec + fir
                elif i == '-':
                    ans = sec - fir
                elif i == '*':
                    ans = sec * fir
                elif i == '/':
                    if sec < 0 and fir < 0:
                        ans = (abs(sec) // abs(fir))
                    elif sec < 0 or fir < 0:
                        ans = -(abs(sec) // abs(fir))
                    else:
                        ans = (abs(sec) // abs(fir))
                
                st.append(str(ans))
            else:
                st.append(i)
        
        return int(st[0])

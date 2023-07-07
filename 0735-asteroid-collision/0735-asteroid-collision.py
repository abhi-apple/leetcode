class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        ans=[]
        for i in ast:
            if i<0 and ans and ans[-1]>0:
                while ans and ans[-1]>0 and ans[-1]<-i:
                    ans.pop()
                if not ans or ans[-1]<0:
                    ans.append(i)
                elif ans[-1]==-i:
                    ans.pop()
            else:
                ans.append(i)
        return ans
                
                    
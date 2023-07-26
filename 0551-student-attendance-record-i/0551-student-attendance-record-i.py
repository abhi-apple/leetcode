class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1:
            return False
        cnt=0
        for i in s:
            if i=='L':
                cnt+=1
                if cnt>2:
                    return False
                
            else:
                cnt=0
            
        return True
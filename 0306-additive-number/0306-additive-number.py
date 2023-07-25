class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)

        if n<3:
            return False
        if len(set(num))==1 and num[0]=='0':
            return True
        def rec(i,jusp,prev,chk):
            # print(i,jusp,prev,chk)
            if i == n:
                if jusp==-1 or prev==-1 or not chk:
                    return False
                return True
            
            if prev==-1:
                if num[i]=='0':
                    if rec(i+1,jusp,0,False):
                        return True
                    return False
                # print('fir')
                for k in range(i,n):
                    if rec(k+1,jusp,int(num[i:k+1]),False):
                        return True
                return False
            elif jusp==-1:
                if num[i]=='0':
                    if rec(i+1,0,prev,False):
                        return True
                    return False
                # print('sfir')
                for k in range(i,n):
                    
                    if rec(k+1,int(num[i:k+1]),prev,False):
                        return True
                return False
            else:
                # print('las')
                if num[i]=='0':
                    return False
                for k in range(i,n):
                    # print((num[i:k+1]),jusp,prev)
                    if int(num[i:k+1])==jusp+prev:
                        
                        if rec(k+1,int(num[i:k+1]),jusp,True):
                            return True
                return False
        return rec(0,-1,-1,False)
                    
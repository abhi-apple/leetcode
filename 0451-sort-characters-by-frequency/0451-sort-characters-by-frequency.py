class Solution:
    def frequencySort(self, s: str) -> str:
        otp=[]
        for i in set(s):
            cnt=s.count(i)
            otp.append(i*cnt)
            
        s=sorted(otp,key=len,reverse=True)
        return "".join(s)

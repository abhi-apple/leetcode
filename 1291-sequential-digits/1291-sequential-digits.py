class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums=[1,2,3,4,5,6,7,8,9]
        n=len(str(low))
        st=int(str(low)[0])
        st=st-1
        ans=[]
        while st+n<10:
            now=''
            for i in nums[st:st+n]:
                now=now+str(i)
            if int(now)<=high and int(now)>=low:
                ans.append(int(now))
            st+=1
        if len(str(low))!=len(str(high)):
            k=len(str(low))
            while k<=len(str(high)):
                k=k+1
                st=0
                # k=len(str(high))
                while st+k<10:
                    now=''
                    for i in nums[st:st+k]:
                        now=now+str(i)
                    if int(now)<=high:
                        ans.append(int(now))
                    st+=1
        return ans
            
            
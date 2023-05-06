class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        st=""
        cnt=1
        for i in range(len(s)):
            st+=s[i]
            if int(st)>k:
                st=""
                st=s[i]
                if int(s[i])>k:
                    return -1
                cnt+=1
        return cnt
                
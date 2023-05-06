class Solution:
    def minGroups(self, inter: List[List[int]]) -> int:
        st=[]
        ed=[]
        for be,en in inter:
            st.append(be)
            ed.append(en)  # corrected variable name
        st.sort()
        ed.sort()
        i=1
        j=0
        cnt=1
        curr_inter=1  # corrected variable name
        while i<len(st):  # corrected inequality
            if st[i]>ed[j]:
                curr_inter-=1  # corrected operation
                j+=1
            else:
                curr_inter+=1  # corrected operation
                i+=1
            cnt=max(curr_inter,cnt)
        return cnt

class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        st=[]
        ins=['(','{','[']
        dic={}
        dic[')']='('
        dic['}']='{'
        dic[']']='['
        for i in range(len(s)):
            if s[i] in ins:
                st.append(s[i])
            else:
                if not st or  dic[s[i]]!=st.pop():
                    return False
        return True if len(st)==0 else False
                
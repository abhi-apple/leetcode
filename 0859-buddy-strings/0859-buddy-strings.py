class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        if not s and not goal:
            return True
        if not s or not goal:
            return False
        if len(s)!=len(goal):
            return False
        if s==goal and len(set(s))!=len(s):
            return True
        dif=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                dif.append(i)

        if len(dif)!=2:
            return False
        tmp=dif[0]
        s[dif[0]],s[dif[1]]=s[dif[1]],s[dif[0]]
        if s!=goal:
            return False
        return True
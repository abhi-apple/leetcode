class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=["A"]
        for i in s:
            if i=="(":
                # if l[-1]==")":
                #     l.pop()
                # else:
                l.append(i)
            if i==")":
                if l[-1]=="(":
                    l.pop()
                else:
                    l.append(i)
        print(l)
        return len(l)-1
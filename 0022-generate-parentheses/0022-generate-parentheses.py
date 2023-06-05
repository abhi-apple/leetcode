class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp={}
        main=[]
        def rec(op,cl,cur):
            if op==n and cl==n:
                main.append(cur)
                return 
            if (op,cl,cur) in dp:
                return dp[(op,cl,cur)]
            if op<n:
                rec(op+1,cl,cur+'(')
            if cl<n and op>=cl+1:
                rec(op,cl+1,cur+')')
            dp[(op, cl, cur)] = True
        rec(0,0,'')
        return main
                
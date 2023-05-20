class Solution:
    def calcEquation(self, eq: List[List[str]], val: List[float], que: List[List[str]]) -> List[float]:
        grp = {}
        for i in range(len(eq)):
            fir = eq[i][0]
            sec = eq[i][1]
            if fir in grp:
                grp[fir].append([sec, val[i]])
            else:
                grp[fir] = [[sec, val[i]]]
            if sec in grp:
                grp[sec].append([fir, 1 / val[i]])
            else:
                grp[sec] = [[fir, 1 / val[i]]]
        
        ans = []
        def dfs(st, tar, tmp, vis):
            if st == tar:
                return tmp
            vis.add(st)
            for node in grp[st]:
                if node[0] not in vis:
                    res = dfs(node[0], tar, tmp * node[1], vis)
                    if res != -1:
                        return res
            return -1
        
        for i in que:
            fir = i[0]
            sec = i[1]
            if fir not in grp or sec not in grp:
                ans.append(-1.0)
                continue
            vis = set()
            tp = dfs(fir, sec, 1.0, vis)
            ans.append(tp)
        
        return ans

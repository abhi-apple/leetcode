class Solution:
    def largestCombination(self, cand: List[int]) -> int:
        dic = {i: 0 for i in range(24)}
        for k in range(len(cand)):
            for i in range(24):
                if (cand[k]>>i) & 1==1:
                    dic[i]+=1
        return max(dic.values())
        
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
            dict = {}
            for i, o in enumerate(order):
                dict[o] = i

            for i in range(1,len(words)):
                pre, cur, flag = words[i-1], words[i], 0
                for j in range(min(len(pre),len(cur))):
                    if dict[pre[j]] < dict[cur[j]]:
                        flag = 1
                        break
                    elif dict[pre[j]] > dict[cur[j]]:
                        return False
                if not flag and len(pre) > len(cur): 
                    return False
            return True

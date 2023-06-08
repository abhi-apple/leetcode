class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        fin = []
        n = len(candidates)
        
        def rec(i, arr):
            if i == n:
                if sum(arr) == target:
                    fin.append(arr)
                return
            rec(i + 1, arr)
            if sum(arr)+candidates[i]<=target:
                rec(i, arr + [candidates[i]])
        
        rec(0, [])
        return fin

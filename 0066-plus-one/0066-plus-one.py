class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs=''
        for i in range(len(digits)):
            strs+=str(digits[i])
        ans=list(str(int(strs)+1))
        print(ans)
        res=[]
        for i in range(len(ans)):
            res.append(int(ans[i]))
        return res
        
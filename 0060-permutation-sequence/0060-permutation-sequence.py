class Solution:
    def getPermutation(self, n: int, k: int) -> str:
            fac=1
            nums=[]
            for i in range(1,n):
                fac=fac*i
                nums.append(i)
            nums.append(n)
            ans=''
            k=k-1
            while True:
                ans=ans+str(nums[int(k//fac)])
                nums.remove(nums[int(k//fac)])
                if len(nums)==0:
                    break;
                k=k%fac
                fac=fac/len(nums)
            return ans
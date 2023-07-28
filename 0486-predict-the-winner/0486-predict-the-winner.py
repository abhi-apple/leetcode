class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp={}
        def rec(i,j,trn):
            if i>j:
                return 0
            dp[(i,j,trn)]=0
            if trn:
                dp[(i,j,trn)]=max(rec(i+1,j,not trn)+nums[i],rec(i,j-1,not trn)+nums[j])
            else:
                dp[(i,j,trn)]=min(rec(i+1,j,not trn),rec(i,j-1,not trn))
            return dp[(i,j,trn)]
        return rec(0,len(nums)-1,True)>=(sum(nums)/2)
                
                
                
                
                
                
                                

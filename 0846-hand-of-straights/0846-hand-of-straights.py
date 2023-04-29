class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand) % k != 0:
            return False
        cnt=Counter(hand)
        ans=sorted(cnt)
        while ans:
            st=ans[0]
            for i in range(st,st+k):
                if cnt[i]==0:
                    return False
                cnt[i]-=1
                if cnt[i]==0:
                    ans.remove(i)
        return True
            
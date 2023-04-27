class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        print(people)
        ans=[[-1,-1] for i in range(len(people))]
        for i in range(len(people)):
            cnt=people[i][1]
            for j in range(len(people)):
                if ans[j][0]==-1 and cnt==0:
                    ans[j][0]=people[i][0]
                    ans[j][1]=people[i][1]
                    break
                elif ans[j][0]==-1 or ans[j][0]>= people[i][0]:
                    cnt-=1
                
        return ans
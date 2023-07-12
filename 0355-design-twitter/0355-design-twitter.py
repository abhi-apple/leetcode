class Twitter:

    def __init__(self):
        self.follodic={}
        self.mstwee=[]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mstwee.append([userId,tweetId])
        if userId not in self.follodic:
            self.follodic[userId]=[userId]
            
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.mstwee)
        # print(self.follodic)
        cnt=0
        ans=[]
        for i in range(len(self.mstwee)-1,-1,-1):
            if cnt<10 and self.mstwee[i][0] in self.follodic[userId]:
                ans.append(self.mstwee[i][1])
                cnt+=1
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follodic:
            self.follodic[followerId].append(followeeId)
        else:
            self.follodic[followerId]=[followeeId,followerId]
            
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follodic and followeeId in self.follodic[followerId]:
            self.follodic[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
class Twitter:

    def __init__(self):
        # Users maps to their posts
        self.time = 0
        self.postToUser = {}
        
        # Users maps to their following
        self.userToUsers = defaultdict(list)

        # All the posts posted by the all the users
        self.tweets = []
        heapq.heapify(self.tweets)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postToUser[tweetId] = userId
        heapq.heappush(self.tweets, (-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        res = []
        popped = []
        while self.tweets and k>0:
            item = heapq.heappop(self.tweets)
            popped.append(item)
            tweetId = item[1]
            tweetPoster = self.postToUser[tweetId] 
            if (tweetPoster in self.userToUsers[userId] or userId == tweetPoster):
                k-=1
                res.append(tweetId)


        for t in popped:
            heapq.heappush(self.tweets, t)


        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userToUsers[followerId]:
            self.userToUsers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToUsers[followerId]:
            self.userToUsers[followerId].remove(followeeId)
        

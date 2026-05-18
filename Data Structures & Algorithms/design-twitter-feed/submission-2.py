class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)
        ans = []
        maxHeap = []
        # first loop to form 10 candidates
        for person in self.followers[userId]:
            if person in self.tweets:
                index = len(self.tweets[person]) - 1
                time, tweetId = self.tweets[person][index]
                heapq.heappush(maxHeap, [time, tweetId, person, index])
        # updating and forming the ans
        while maxHeap and len(ans) < 10:
            time, tweetId, person, index = heapq.heappop(maxHeap)
            ans.append(tweetId)
            if index > 0:
                time, tweetId = self.tweets[person][index -1]
                heapq.heappush(maxHeap, [time, tweetId, person, index-1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

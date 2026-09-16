class Twitter:
    # problem uses count to identify the tweets rather than a random uuid
    def __init__(self):
        import heapq
        from collections import defaultdict

        self.followMap=defaultdict(set)
        # This is a hashset of userIds mapped to their who they follow
        self.tweetMap=defaultdict(list)
        # 
        
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count-=1
        # Count down, because we want the newest stuff to be at the top of the minheap?


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap=[]
        result=[]

        self.followMap[userId].add(userId)
        # Include the user themselves in their followmap.
        # It just needs to happen any time but it's being done in the news feed call
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        while min_heap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
        return result
        

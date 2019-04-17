import collections
class Twitter:
    def __init__(self):
        self.dic = collections.defaultdict(list)
        self.timer = 0
        self.followDict = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.dic[userId].append([tweetId, self.timer])
        self.timer += 1

    def getNewsFeed(self, userId: int):
        News = []
        News += self.dic[userId]
        for follower in self.followDict[userId]:
            News += self.dic[follower]
        News = sorted(News, key=lambda x:x[1], reverse=True)
        return [news[0] for news in News][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followDict[followerId] and followerId != followeeId:
            self.followDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDict[followerId]:
            self.followDict[followerId].remove(followeeId)

T = Twitter()
T.postTweet(1,1)
T.follow(1,2)
T.follow(1,3)
T.follow(2,4)
T.postTweet(2,2)
T.postTweet(3,8)
print(T.getNewsFeed(1))
T.unfollow(1,3)
print(T.getNewsFeed(1))
# Qus:https://leetcode.com/problems/design-twitter/

from collections import defaultdict
from heapq import heappop, heappush, heapify


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followerMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        # print self.time
        # print "folo ",self.followerMap
        # print "tweet",self.tweetsMap
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetsMap[userId].append((self.time, tweetId))

        self.time -= 1

    def getNewsFeed(self, userId):
        # print self.time
        # print "folo ",self.followerMap
        # print "tweet",self.tweetsMap
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap = self.tweetsMap[userId][:]
        out = []

        for followee in self.followerMap[userId]:
            heap.extend(self.tweetsMap[followee][:])

        # use heapify
        heapify(heap)
        # print "heap",heap
        # now pop out most recent tweets
        i = 0
        while(heap != [] and i < 10):
            out.append(heappop(heap)[1])
            i += 1

        return out[:]

    def follow(self, followerId, followeeId):
        # print self.time
        # print "folo ",self.followerMap
        # print "tweet",self.tweetsMap
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # follower id should not be same as followeeId
        if(followerId == followeeId):
            return

        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        # print self.time
        # print "folo ",self.followerMap
        # print "tweet",self.tweetsMap
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if(followerId in self.followerMap):
            self.followerMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

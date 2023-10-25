#vsCode

import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        # Initialize your Twitter data structure here.
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Manually input userId and tweetId for posting a tweet
        userId = 1  # Change to your desired userId
        tweetId = 101  # Change to your desired tweetId

        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Manually input userId to get the news feed
        userId = 1  # Change to your desired userId

        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Manually input followerId and followeeId to establish a follow relationship
        followerId = 1  # Change to your desired followerId
        followeeId = 2  # Change to your desired followeeId

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Manually input followerId and followeeId to remove a follow relationship
        followerId = 1  # Change to your desired followerId
        followeeId = 2  # Change to your desired followeeId

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Create an instance of the Twitter class
twitter = Twitter()

# Perform Twitter actions and print the results as needed

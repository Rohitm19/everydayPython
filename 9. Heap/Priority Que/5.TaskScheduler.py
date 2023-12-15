#neetCode
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


# Greedy algorithm
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))
#vsCode

import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Manually input the list of tasks (as strings) and the value of 'n'
        # For example, tasks = ["A", "A", "B", "B", "B", "C"] and n = 2
        tasks = ["A", "A", "B", "B", "B", "C"]  # Change to your desired tasks
        n = 2  # Change to your desired 'n'

        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + sum(map(lambda count: count == max_count, counter.values()))

        return max(min_time, len(tasks)

# Create an instance of the Solution class and call the leastInterval function
solution = Solution()
minimum_time = solution.leastInterval(tasks, n)

# Print the minimum time needed to complete the tasks
print("Minimum time:", minimum_time)
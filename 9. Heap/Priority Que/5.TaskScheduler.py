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
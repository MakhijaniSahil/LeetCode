# LeetCode 621 - Task Scheduler
# Approach: Greedy + Max Heap + Cooldown Queue
# Time: O(n log k), where k = number of unique tasks (≤ 26)
# Space: O(1) (since there are at most 26 task types)

import heapq
from collections import Counter, deque


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Count frequency of each task
        map = Counter(tasks)
        # Use max heap to always schedule the most frequent task available
        maxHeap = [(-v, k) for k, v in map.items()]
        heapq.heapify(maxHeap)
        # Queue to keep track of cooldown: [remaining_count, task, available_time]
        q = deque()
        time = 0  # Current time
        while maxHeap or q:
            time += 1  # Increment time for each scheduling slot
            if maxHeap:
                v, k = heapq.heappop(maxHeap)  # Get most frequent available task
                v += 1  # Decrement count (since v is negative)
                if v < 0:  # If there are more occurrences of this task
                    t = time + n  # Next available time for this task
                    q.append([v, k, t])  # Put task in cooldown
            # If a task's cooldown is over, push it back to heap
            if q and q[0][2] == time:
                v, k, t = q.popleft()
                heapq.heappush(maxHeap, (v, k))
        # Return total time units needed
        return time

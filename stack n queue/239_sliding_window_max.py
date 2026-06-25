"""
LeetCode 239 - Sliding Window Maximum
Approach:
- Maintain a monotonic decreasing deque of indices.
- Remove smaller values from the back because they can never become the window maximum.
- The front of the deque always stores the index of the current window maximum.
Time: O(n)
Space: O(k)
"""

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Deque stores indices in decreasing order of their values.
        q = deque()

        res = []

        # Expand the window one index at a time.
        for i in range(len(nums)):
            # Remove smaller elements that cannot be maximum anymore.
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            # Remove the index that just moved out of the window.
            if q[0] == i - k:
                q.popleft()

            # Once the first full window is formed, record its maximum.
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

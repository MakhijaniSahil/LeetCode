"""
LeetCode 155 - Min Stack
Approach:
- Use one stack for all values and another stack for the minimum at each level.
- On every push, store the smaller value between the new value and previous minimum.
- The top of the min stack always gives the current minimum in O(1).
Time: O(1) for push, pop, top, and getMin
Space: O(n)
"""

from collections import deque


class MinStack(object):

    def __init__(self):
        # Main stack stores all pushed values.
        self.s = deque()
        # min_s[i] stores the minimum value up to s[i].
        self.min_s = deque()

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        # Push value normally and track the running minimum.
        self.s.append(value)
        self.min_s.append(value if not self.min_s else min(value, self.min_s[-1]))

    def pop(self):
        """
        :rtype: None
        """
        # Pop from both stacks to keep their levels aligned.
        self.min_s.pop()
        return self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        # Top of the main stack is the latest pushed value.
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # Top of the min stack is the minimum in the current stack.
        return self.min_s[-1]

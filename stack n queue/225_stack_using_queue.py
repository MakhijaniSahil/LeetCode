"""
LeetCode 225 - Implement Stack using Queues
Approach:
- Use a deque as the underlying container for stack operations.
- Push elements to the back and read/remove from the back for LIFO order.
Time: O(1) for push, pop, top, and empty
Space: O(n)
"""

from collections import deque


class MyStack(object):

    def __init__(self):
        # Store elements in stack order.
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Add the newest element to the top of the stack.
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Remove and return the current top element.
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Last element is the top of the stack.
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # Stack is empty when no elements are stored.
        return False if len(self.stack) else True

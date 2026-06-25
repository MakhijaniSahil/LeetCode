"""
LeetCode 232 - Implement Queue using Stacks
Approach:
- Use a list as the backing container for queue operations.
- Push elements to the back and remove/read from the front for FIFO order.
Time: O(1) for push, peek, and empty; O(n) for pop
Space: O(n)
"""


class MyQueue(object):

    def __init__(self):
        # Store elements in queue order.
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Add the newest element to the back of the queue.
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Remove and return the front element.
        return self.q.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        # First element is the front of the queue.
        return self.q[0]    

    def empty(self):
        """
        :rtype: bool
        """
        # Queue is empty when no elements are stored.
        return len(self.q) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

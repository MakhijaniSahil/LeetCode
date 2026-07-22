"""
LeetCode 1291 - Sequential Digits
Approach 1: Brute Force by Length
- Try every digit length between the bounds.
- Build sequential numbers and keep the ones in range.
Time: O(1)
Space: O(1)

Approach 2: BFS Generation
- Start from 1 through 9.
- Extend each number by appending the next consecutive digit.
- Collect values that fall within the target range.
Time: O(1)
Space: O(1)
"""

from collections import deque


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # Collect valid sequential numbers here.
        res = []

        # Limit candidate lengths to the number of digits in the bounds.
        l = len(str(low))
        h = len(str(high))

        for digits in range(l, h + 1):
            for start in range(1, 9):
                if start + digits > 10:
                    break
                num = start
                prev = start

                for i in range(digits - 1):
                    num = num * 10
                    prev += 1
                    num += prev

                if low <= num <= high:
                    res.append(num)

        return res


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # Queue stores the next sequential numbers to expand.
        res = []
        q = deque(range(1, 10))

        # Generate numbers level by level.
        while q:
            n = q.popleft()
            if n > high:
                continue

            if low <= n <= high:
                res.append(n)

            last = n % 10
            if last < 9:
                q.append(n * 10 + (last + 1))

        return res

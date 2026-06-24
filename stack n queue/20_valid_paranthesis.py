"""
LeetCode 20 - Valid Parentheses
Approach:
- Use a stack to store opening brackets.
- For every closing bracket, check whether it matches the latest opening bracket.
- The string is valid only if all brackets match and the stack ends empty.
Time: O(n)
Space: O(n)
"""

from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack stores unmatched opening brackets.
        stack = deque()

        # Map each closing bracket to its matching opening bracket.
        pair = {")": "(", "]": "[", "}": "{"}

        # Process each bracket from left to right.
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # A closing bracket cannot match if no opening bracket exists.
                if not stack:
                    return False

                # Top of stack must be the matching opening bracket.
                if stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False

        # All opening brackets must be matched.
        return not stack
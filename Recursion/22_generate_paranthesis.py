"""
LeetCode 22 - Generate Parentheses
Approach: Backtracking with counts of open and closed parentheses
Time: O(4^n / sqrt(n))
Space: O(n)
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Current construction and final result list
        stack = []
        res = []

        def bt(open, close):
            # When both counts reach n, we have a valid string
            if open == close == n:
                res.append("".join(stack))
                return

            # Add an opening parenthesis if we still have one available
            if open < n:
                stack.append("(")
                bt(open + 1, close)
                stack.pop()

            # Add a closing parenthesis only if it keeps the string valid
            if close < open:
                stack.append(")")
                bt(open, close + 1)
                stack.pop()

        bt(0, 0)
        return res

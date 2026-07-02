"""
LeetCode 1614 - Maximum Nesting Depth of the Parentheses
Approach:
- Scan the string, track current open-parentheses depth
- Update the maximum depth seen while encountering '('
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_cnt = 0
        max_depth = 0

        # Iterate characters, increasing depth on '(' and decreasing on ')'.
        for c in s:
            if c == "(":
                open_cnt += 1
                # Record the peak depth after an opening parenthesis.
                max_depth = max(max_depth, open_cnt)
            elif c == ")":
                # Close one level of nesting.
                open_cnt -= 1

        return max_depth

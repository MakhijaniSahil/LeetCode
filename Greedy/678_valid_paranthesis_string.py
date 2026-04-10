# LeetCode 678 - Valid Parenthesis String
# Approach 1: Stacks for '(' and '*' indices
# Time: O(n)
# Approach 2: Greedy range tracking (leftMin/leftMax)
# Time: O(n)
# Space: O(1) for greedy approach


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Indices of unmatched '(' characters.
        stack = []
        # Indices of '*' characters that can act as '(', ')' or empty.
        stars = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            elif s[i] == "*":
                stars.append(i)

            else:
                # Match ')' with latest '(' first, then with '*' if needed.
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        # Remaining '(' must be matched by '*' that appear after them.
        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                return False

        # Valid only if no unmatched '(' remain.
        return not stack


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # leftMin/leftMax track possible range of open '(' count.
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                # '*' can be ')' (leftMin-1) or '(' (leftMax+1).
                leftMin -= 1
                leftMax += 1

            # Too many ')' even in best case.
            if leftMax < 0:
                return False
            # leftMin cannot go below 0 (treat extra '*' as empty).
            if leftMin < 0:
                leftMin = 0

        # Valid if we can finish with exactly 0 open parentheses.
        return leftMin == 0
